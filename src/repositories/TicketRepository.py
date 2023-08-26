from src.models.Ticket import Ticket,db
from sqlalchemy import and_
import string    
import random
class TicketRepository:
  def getAllTickets(self):
    return Ticket.query.filter(Ticket.event_id.isnot(None)).all()  
  def getAllTicketByUserId(self,user_id):
    return Ticket.query.filter(and_(Ticket.user_id == user_id, Ticket.event_id.isnot(None))).all()  
  def getAllTicketByEventId(self,event_id):
    return Ticket.query.filter_by(event_id=event_id).all()
  
  def createNewTicket(self,data,user_id):
    newTicket = Ticket(
      event_id=data['event_id'], 
      user_id=user_id,
      ticket_code=''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))    ,
      )
    db.session.add(newTicket)
    db.session.commit()
    return newTicket
  def attendTicket(self,code):
    ticket = Ticket.query.filter_by(ticket_code=code).first()
    if(not ticket) :return False
    ticket.is_attended = True
    db.session.commit()
    return ticket
  def getTicketByCode(self,code):
    return Ticket.query.filter(and_(Ticket.ticket_code == code, Ticket.event_id.isnot(None))).first()