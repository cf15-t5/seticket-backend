from flask import Blueprint
from flask import request
from src.services.UserService import UserService as UserService
import src.utils.getResponse as Response  

UserApp = Blueprint('UserApp', __name__,)
userService =  UserService()

@UserApp.route('/', methods=['GET'])
def index():
  users = userService.getAllUser()
  return Response.success(users,"success get all user")
  
@UserApp.route('/create', methods=['POST'])
def create():
  req = request.json
  result = userService.createNewUser(req)
  if(result['status'] == 'failed'):
   return Response.error(result['data'],result['code'])
  return Response.success(result['data'],"success create new user")