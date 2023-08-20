from flask import Blueprint
from flask import request,g
from src.services.EventService import EventService
from src.middlewares.AuthMiddleware import isAuthenticated
import src.utils.getResponse as Response  

EventApp = Blueprint('EventApp', __name__,)
eventService =  EventService()

@EventApp.route('/', methods=['GET'])
@isAuthenticated
def index():
  result = eventService.getAllEvent()
  return Response.success(result['data'],"success get all events")

@EventApp.route('/', methods=['POST'])
@isAuthenticated
def store():
  result = eventService.createEvent(request.form,file=request.files,user_id=g.user['user_id'])
  if(result['status'] == 'failed'):
    return Response.error(result['data'],result['code'])
  
  return Response.success(result['data'],"success create new event")


@EventApp.route('/verify', methods=['POST'])
@isAuthenticated
def verify():  
  return Response.success([],"success verify user")


@EventApp.route('/<id>', methods=['PUT'])
@isAuthenticated
def update(id):
  result = eventService.updateEvent(id,request.form,file=request.files,user_id=g.user['user_id'])
  if(result['status'] == 'failed'):
    return Response.error(result['data'],result['code'])
  
  return Response.success(result['data'],"success update event")


@EventApp.route('/<id>/delete', methods=['DELETE'])
@isAuthenticated
def delete(id):
  result = eventService.deleteEvent(id)
  if(result['status'] == 'failed'):
    return Response.error(result['data'],result['code'])
  
  return Response.success(result['data'],"success delete event")