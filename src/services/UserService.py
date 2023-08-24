from src.repositories.UserRepository import UserRepository
from src.repositories.TransactionRepository import TransactionRepository
from src.utils.errorHandler import errorHandler
from src.utils.validator.UserValidator import (
    UpdateProfileValidator,
    UpdateBalanceValidator,
)
from src.utils.convert import queryResultToDict
from src.services.Service import Service

userRepository = UserRepository()
transactionRepository = TransactionRepository()


class UserService(Service):
    @staticmethod
    def failedOrSuccessRequest(status, code, data):
        return {
            "status": status,
            "code": code,
            "data": data,
        }

    def getAllUser(self):
        try:
            data = userRepository.getAllUser()
            return UserService.failedOrSuccessRequest(
                "success", 200, queryResultToDict(data)
            )
        except Exception as e:
            return UserService.failedOrSuccessRequest("failed", 500, str(e))

    def updateProfile(self, data, id):
        try:
            validate = UpdateProfileValidator(**data)
            if not validate:
                return self.failedOrSuccessRequest("failed", 400, "Validation failed")
            user = userRepository.updateProfile(id=id, data=data)
            if not user:
                return self.failedOrSuccessRequest("failed", 400, "user not found")
            return self.failedOrSuccessRequest(
                "success", 200, queryResultToDict([user])[0]
            )
        except ValueError as e:
            return self.failedOrSuccessRequest(
                "failed", 500, " ".join(map(str, e.args))
            )

    def topup(self, id, data):
        try:
            validate = UpdateBalanceValidator(**data)
            if not validate:
                return self.failedOrSuccessRequest("failed", 400, "Validation failed")
            user = userRepository.updateBalance(
                id=id, nominal=data["nominal"], operator="plus"
            )
            transactionRepository.createNewTransaction(
                type="topup", user_id=id, nominal=data["nominal"]
            )
            return self.failedOrSuccessRequest(
                "success", 200, queryResultToDict([user])[0]
            )
        except ValueError as e:
            return self.failedOrSuccessRequest(
                "failed", 500, " ".join(map(str, e.args))
            )

    def withdraw(self, id, data):
        try:
            validate = UpdateBalanceValidator(**data)
            if not validate:
                return self.failedOrSuccessRequest("failed", 400, "Validation failed")
            user = userRepository.getUserById(user_id=id)

            if user.balance < data["nominal"]:
                return self.failedOrSuccessRequest("failed", 400, "balance not enough")

            user = userRepository.updateBalance(
                id=id, nominal=data["nominal"], operator="minus"
            )
            transactionRepository.createNewTransaction(
                type="withdraw", user_id=id, nominal=data["nominal"]
            )
            return self.failedOrSuccessRequest(
                "success", 200, queryResultToDict([user])[0]
            )
        except ValueError as e:
            return self.failedOrSuccessRequest(
                "failed", 500, " ".join(map(str, e.args))
            )

    def searchUser(self, id):
        try:
            user = userRepository.getUserById(id)
            if not user:
                return self.failedOrSuccessRequest("failed", 400, "User not found")
            else:
                return self.failedOrSuccessRequest("success", 200, user)
        except Exception as e:
            return self.failedOrSuccessRequest("failed", 500, str(e))
