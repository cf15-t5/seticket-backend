
from src.repositories.TicketRepository import TicketRepository
from src.repositories.UserRepository import UserRepository
from src.repositories.EventRepository import EventRepository
from src.repositories.TransactionRepository import TransactionRepository
from src.utils.convert import queryResultToDict
from src.services.Service import Service
from src.utils.validator.TicketValidator import CreateNewTicketValidator,AttendTicketValidator
from src.utils.errorHandler import errorHandler
from src.utils.sendMail import sendMail
from datetime import datetime
from flask import render_template

ticketRepository = TicketRepository()    
userRepository = UserRepository()
eventRepository = EventRepository()
transactionRepository = TransactionRepository()

class TicketService(Service):
    @staticmethod
    def failedOrSuccessRequest(status, code, data):
        return {
            'status': status,
            "code": code,
            'data': data,
        }
    def _validationCreateNewTicket(self,event,user):
        if(not event):
            return self.failedOrSuccessRequest('failed', 400, 'event not found')
        if (len(event.tickets) >= event.number_of_ticket):
            return self.failedOrSuccessRequest('failed', 400, 'ticket sold out')
        today = datetime.today()
        if (event.date_of_event.date() < today.date()):
            return self.failedOrSuccessRequest('failed', 400, 'event has passed')
        if([item for item in event.tickets if item.user_id ==user.user_id]):
            return self.failedOrSuccessRequest('failed', 400, 'you already have ticket for this event')
        if user.balance < event.price:
            return self.failedOrSuccessRequest('failed', 400, 'balance not enough')
        return True
    def _purchaseTicket(self,data):
         date = data.event.date_of_event
         event_date = date.strftime("%d %B %Y")
         event_time = date.strftime("%H:%M") 
         return render_template(
                'html/mail.html',
                code=data.ticket_code,
                event_name=data.event.title,
                location=data.event.address,
                name=data.user.name,
                date=event_date,
                time=event_time)
    def _soldOutEvent(self,data):
        return render_template(
                'html/soldOutEventNotification.html',
                event_name=data.title,
                location=data.address,
                event_date=data.date_of_event.strftime("%d %B %Y"),
                event_time=data.date_of_event.strftime("%H:%M"),
                ticket_count=len(data.tickets),
                category=data.category.name,
                name=data.user.name,
                image_url=f"https://api-seticket.aprnna.me/{data.poster_path.replace('public/','')}"
                )
    def _sendNotification(self,templates,to,subject):
         sendMail(
            templates=templates,
            subject=subject,
            to=to
            )
         return True
    def getAllTickets(self):
        try:
            data = ticketRepository.getAllTickets()
            return self.failedOrSuccessRequest('success', 200, queryResultToDict(data,['user','event']))
        except Exception as e:
            return self.failedOrSuccessRequest('failed', 500, str(e))
    
    def createNewTicket(self,data,user_id):
        try:
            validate = CreateNewTicketValidator(**data)
            
            if(not validate):
                return self.failedOrSuccessRequest('failed', 400, validate.errors())
            event = eventRepository.getEventById(data['event_id'])
            user = userRepository.getUserById(user_id)
            
            validation = self._validationCreateNewTicket(event,user)
            if(validation != True): return validation
            userRepository.updateBalance(id=user_id,nominal=event.price,operator='minus')
            userRepository.updateBalance(id=event.user_id,nominal=event.price,operator='plus')
            data = ticketRepository.createNewTicket(data,user_id)
            transactionRepository.createNewTransaction(
                type='buy',
                user_id=user_id,
                nominal=event.price,
                ticket_id=data.ticket_id
                )
            # if():
            # print()
            if(len(event.tickets) >= event.number_of_ticket-1):
                
                self._sendNotification(subject="Event Sold Out" , templates=self._soldOutEvent(event),to=event.user.email)
            self._sendNotification(subject="Ticket Event",templates=self._purchaseTicket(data),to=user.email)
            
            return self.failedOrSuccessRequest('success', 200, queryResultToDict([data])[0])
        except ValueError as e:
          return self.failedOrSuccessRequest('failed', 400, errorHandler(e.errors()))
        except Exception as e:
            return self.failedOrSuccessRequest('failed', 500, str(e))
        
    def getTicketByUserId(self,user_id):
        try:
            data = ticketRepository.getAllTicketByUserId(user_id)
            return self.failedOrSuccessRequest('success', 200, queryResultToDict(data,['user','event']))
        except Exception as e:
            return self.failedOrSuccessRequest('failed', 500, str(e))
    def attendTicket(self,data,user_id):
        try:
            validate= AttendTicketValidator(**data)
            if(not validate):
                return self.failedOrSuccessRequest('failed', 400, validate.errors())
            ticket = ticketRepository.getTicketByCode(data['ticket_code'])
            if(not ticket):
                return self.failedOrSuccessRequest('failed', 400, 'ticket not found')
            if(ticket.event.user_id != user_id):
                return self.failedOrSuccessRequest('failed', 400, 'ticket not belong to you')
            if(ticket.is_attended):
                return self.failedOrSuccessRequest('failed', 400, 'ticket already attended')
            ticket = ticketRepository.attendTicket(data['ticket_code'])
            return self.failedOrSuccessRequest('success', 200, queryResultToDict([ticket])[0])
        
        except ValueError as e:
            return self.failedOrSuccessRequest('failed', 400, errorHandler(e.errors()))
        except Exception as e:
            return self.failedOrSuccessRequest('failed', 500, str(e))
