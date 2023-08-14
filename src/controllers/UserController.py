from flask import Blueprint, jsonify
from flask import request
from  src.models.User import User as UserModel
from src.services.UserService import UserService as UserService
import src.utils.getResponse as Response  
UserApp = Blueprint('UserApp', __name__)
userService =  UserService()
import sys
@UserApp.route('/', methods=['GET'])
def index():
  users = UserModel.query.all() or []
  return jsonify(users)
  
@UserApp.route('/create', methods=['POST'])
def create():
  req = request.json
  result = userService.createNewUser(req)
  if(result['status'] == 'failed'):
   return Response.error(result['data'],result['code'])
  return Response.success(result['data'],"success create new user")