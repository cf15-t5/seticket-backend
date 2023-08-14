from src.utils.validator.UserValidator import UserValidator
from src.utils.errorHandler import errorHandler
from src.repositories.UserRepository import UserRepository

user_repository = UserRepository()    


class AuthService():
    @staticmethod
    def failedOrSuccessRequest(status, code, data):
        return {
            'status': status,
            "code": code,
            'data': data,
        }
    
    def registerUser(self, data):
        try:
            isEmailExist = user_repository.getUserByEmail(data['email'])
            if isEmailExist:
                return self.failedOrSuccessRequest('failed', 400,('email already exist'))
            validate = UserValidator(**data)
            if not validate:
                return self.failedOrSuccessRequest('failed', 400, 'Validation failed')
            newUser = user_repository.createNewUser(data)
            return self.failedOrSuccessRequest('success', 201, newUser)
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
