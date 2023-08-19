from flask import Blueprint
from flask import request
from src.services.UserService import UserService as UserService
from src.middlewares.AuthMiddleware import isAuthenticated
import src.utils.getResponse as Response  

UserApp = Blueprint('UserApp', __name__,)
userService =  UserService()

@UserApp.route('/', methods=['GET'])
@isAuthenticated
def index():
  result = userService.getAllUser()
  return Response.success(result['data'],"success get all user")