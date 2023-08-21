from flask import Blueprint
from flask import request,g
from src.services.CategoryService import CategoryService
from src.middlewares.AuthMiddleware import isAuthenticated
import src.utils.getResponse as Response  

CategoryApp = Blueprint('CategoryApp', __name__,)
categoryService =  CategoryService()

@CategoryApp.route('/', methods=['GET'])
def index():
  
  result = categoryService.getAllCategories()
  return Response.success(result['data'],"success get all events")

@CategoryApp.route('/', methods=['POST'])
@isAuthenticated
def store():
  result = categoryService.createCategory(request.json)
  if(result['status'] == 'failed'):
    return Response.error(result['data'],result['code'])
  
  return Response.success(result['data'],"success create new event")

@CategoryApp.route('/<id>', methods=['PUT'])
@isAuthenticated
def update(id):
  result = categoryService.updateCategory(id,request.json)
  if(result['status'] == 'failed'):
    return Response.error(result['data'],result['code'])
  
  return Response.success(result['data'],"success update event")


@CategoryApp.route('/<id>/delete', methods=['DELETE'])
@isAuthenticated
def delete(id):
  result = categoryService.deleteCategory(id)
  if(result['status'] == 'failed'):
    return Response.error(result['data'],result['code'])
  
  return Response.success(result['data'],"success delete event")