
from src.repositories.UserRepository import UserRepository
import sys
user_repository = UserRepository()    

class UserService:
    @staticmethod
    def failedOrSuccessRequest(status, code, data):
        return {
            'status': status,
            "code": code,
            'data': data,
        }
    
    def getAllUser(self):
        try:
            data = user_repository.getAllUser()
            return UserService.failedOrSuccessRequest('success', 200, data)
        except Exception as e:
            return UserService.failedOrSuccessRequest('failed', 500, str(e))
    
   