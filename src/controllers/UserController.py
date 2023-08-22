from flask import Blueprint,request,g
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

@UserApp.route('/update-profile', methods=['post'])
@isAuthenticated
def updateProfile():  
  req = request.json
  result = userService.updateProfile(data=req,id=g.user['user_id'])
  if(result['status'] == 'failed'):
   return Response.error(result['data'],result['code'])
  return Response.success(result['data'],"success update profile user")

@UserApp.route('/topup', methods=['post'])
@isAuthenticated
def topup():  
  req = request.json
  result = userService.topup(data=req,id=g.user['user_id'])
  if(result['status'] == 'failed'):
   return Response.error(result['data'],result['code'])
  return Response.success(result['data'],"success topup user")

@UserApp.route('/withdraw', methods=['post'])
@isAuthenticated
def withdraw():  
  req = request.json
  result = userService.withdraw(data=req,id=g.user['user_id'])
  if(result['status'] == 'failed'):
   return Response.error(result['data'],result['code'])
  return Response.success(result['data'],"success withdraw user")