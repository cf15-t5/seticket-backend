
from src.repositories.UserRepository import UserRepository
from src.utils.convert import transformToDictList

userRepository = UserRepository()    

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
            data = userRepository.getAllUser()
            return UserService.failedOrSuccessRequest('success', 200, transformToDictList(data))
        except Exception as e:
            return UserService.failedOrSuccessRequest('failed', 500, str(e))
    
   