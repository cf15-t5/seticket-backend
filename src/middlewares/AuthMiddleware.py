import src.utils.jwt as jwt
import src.utils.getResponse as response
from flask import request, g
from src.repositories.UserRepository import UserRepository
from src.utils.permission import check_role_is_have_access
user_repository = UserRepository()

def isAuthenticated():
    def decorator(func):
        def wrapper(*args, **kwargs):
            if(request.headers.get('Authorization') == None):
                return response.error(message="Unauthorized",errors=None,status_code=401)
            else:
              token = request.headers.get('Authorization').split(" ")[1]
              try:
                decode = jwt.decode(token)
                user = user_repository.getUserById(decode['user_id']) 
                is_have_access = check_role_is_have_access(user.role,request.path)
                if(not is_have_access):
                  return response.error(message="Forbidden",errors=None,status_code=403)
                g.user= dict(user)
                return func(*args, **kwargs)
              except Exception :
                return response.error(message="Unauthorized",errors=None,status_code=401)
        return wrapper
    return decorator