from src.utils.validator.AuthValidator import RegisterValidator, LoginValidator
from src.utils.errorHandler import errorHandler
from src.repositories.UserRepository import UserRepository
import bcrypt
import src.utils.jwt as jwt 
user_repository = UserRepository()    

import sys
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
            
            validate = RegisterValidator(**data)
            if not validate:
                return self.failedOrSuccessRequest('failed', 400, 'Validation failed')
            
            newUser = user_repository.createNewUser(data)
            
            return self.failedOrSuccessRequest('success', 201, newUser)
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
        
    def login(self,data):
        try:
            validate = LoginValidator(**data)
            if not validate:
                return self.failedOrSuccessRequest('failed', 400, 'Validation failed')
            
            user = user_repository.getUserByEmail(data['email'])
            isPasswordMatch = bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8') )
            if not user or not isPasswordMatch:
                return self.failedOrSuccessRequest('failed', 400, 'user not found')
            
            userDict = dict(user)
            
            userDict['token'] = jwt.encode(userDict)
            return self.failedOrSuccessRequest('success', 200,userDict)
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))