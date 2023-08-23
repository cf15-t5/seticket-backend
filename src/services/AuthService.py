from src.utils.validator.AuthValidator import RegisterValidator, LoginValidator,VerifyValidator
from src.utils.errorHandler import errorHandler
from src.repositories.UserRepository import UserRepository
import bcrypt
import src.utils.jwt as jwt 
from src.utils.convert import queryResultToDict
user_repository = UserRepository()    
from  src.services.Service import Service
class AuthService(Service):
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
            
            return self.failedOrSuccessRequest('success', 201, queryResultToDict([newUser])[0])
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
        
    def login(self,data):
        try:
            validate = LoginValidator(**data)
            if not validate:
                return self.failedOrSuccessRequest('failed', 400, 'Validation failed')
            
            user = user_repository.getUserByEmail(data['email'])
            if not user:
                return self.failedOrSuccessRequest('failed', 400, 'user not found')
            isPasswordMatch = bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8') )
            if not user or not isPasswordMatch:
                return self.failedOrSuccessRequest('failed', 400, 'user not found')
            print(user.status)
            if(user.status == 'INACTIVE'):return  self.failedOrSuccessRequest('failed', 400, 'user not verified')
            user_dict = queryResultToDict([user])[0]
            
            user_dict['token'] = jwt.encode(user_dict)
            return self.failedOrSuccessRequest('success', 200,user_dict)
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
        
    def verifyEO(self,data):
        try:
            user = user_repository.getUserById(data['user_id'])
            if not user:
                return self.failedOrSuccessRequest('failed', 400, 'user not found')
            
            user.status = 'ACTIVE'
            user_repository.commit()
            return self.failedOrSuccessRequest('success', 200, queryResultToDict([user])[0])
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
    def verify(self,data):
        try:
            validate = VerifyValidator(**data)
            if not validate:
                return self.failedOrSuccessRequest('failed', 400, 'Validation failed')
            user = user_repository.verifyUser(data['user_id'],data['status'])
            if not user:
                return self.failedOrSuccessRequest('failed', 400, 'user not found')
            return self.failedOrSuccessRequest('success', 200, queryResultToDict([user])[0])
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))