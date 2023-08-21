from flask import Blueprint
from flask import request,g
from src.services.TicketService import TicketService
from src.middlewares.AuthMiddleware import isAuthenticated
import src.utils.getResponse as Response  

TicketApp = Blueprint('TicketApp', __name__,)
ticketService =  TicketService()

@TicketApp.route('/', methods=['GET'])
@isAuthenticated
def index():
  
  result = ticketService.getAllTickets()
  return Response.success(result['data'],"success get all Tickets")

@TicketApp.route('/', methods=['POST'])
@isAuthenticated
def store():
  result = ticketService.createNewTicket(request.json,g.user['user_id'])
  if(result['status'] == 'failed'):
    return Response.error(result['data'],result['code'])
  return Response.success(result['data'],"success create new event")


@TicketApp.route('/<id>/delete', methods=['DELETE'])
@isAuthenticated
def delete(id):
  result = ticketService.deleteCategory(id)
  if(result['status'] == 'failed'):
    return Response.error(result['data'],result['code'])
  
  return Response.success(result['data'],"success delete event")