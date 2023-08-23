from flask import Blueprint,request,g
from src.services.TransactionService import TransactionService 
from src.middlewares.AuthMiddleware import isAuthenticated
import src.utils.getResponse as Response  

TransactionApp = Blueprint('TransactionApp', __name__,)
transactionService =  TransactionService()

@TransactionApp.route('/', methods=['GET'])
@isAuthenticated
def index():
  result = transactionService.getAllTransactions()
  return Response.success(result['data'],"success get all user")

@TransactionApp.route('/my', methods=['GET'])
@isAuthenticated
def myTransaction():
  result = transactionService.getTransactionByUserId(user_id=g.user['user_id'])
  return Response.success(result['data'],"success get all user")

@TransactionApp.route('/<user_id>', methods=['GET'])
@isAuthenticated
def getTransactionByUserId(user_id):
  result = transactionService.getTransactionByUserId(user_id=user_id)
  if(result['status'] == 'failed'):
    return Response.error(result['data'],result['code'])
  return Response.success(result['data'],"success get all user")