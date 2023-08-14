from flask import Blueprint
from flask import request
from src.services.AuthService import AuthService as AuthService
import src.utils.getResponse as Response  

AuthApp = Blueprint('AuthApp', __name__)
authService =  AuthService()

@AuthApp.route('/login', methods=['GET'])
def index():
  users = []
  return Response.success(users,"success get all user")
  
@AuthApp.route('/register', methods=['POST'])
def register():
  req = request.json
  result = authService.registerUser(req)
  if(result['status'] == 'failed'):
   return Response.error(result['data'],result['code'])
  return Response.success(result['data'],"success create new user")