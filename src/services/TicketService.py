
from src.repositories.TicketRepository import TicketRepository
from src.repositories.UserRepository import UserRepository
from src.repositories.EventRepository import EventRepository
from src.utils.convert import queryResultToDict
from src.services.Service import Service
from src.utils.validator.TicketValidator import CreateNewTicketValidator
from src.utils.errorHandler import errorHandler
from src.utils.sendMail import sendMail

ticketRepository = TicketRepository()    
userRepository = UserRepository()
eventRepository = EventRepository()

class TicketService(Service):
    @staticmethod
    def failedOrSuccessRequest(status, code, data):
        return {
            'status': status,
            "code": code,
            'data': data,
        }
    
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
            
            user = userRepository.getUserById(user_id)
            event = eventRepository.getEventById(data['event_id'])
            if(not event):
                return self.failedOrSuccessRequest('failed', 400, 'event not found')
            if user.balance < event.price:
                return self.failedOrSuccessRequest('failed', 400, 'balance not enough')
            userRepository.updateBalance(id=user_id,nominal=event.price,operator='minus')
            userRepository.updateBalance(id=event.user_id,nominal=event.price,operator='plus')
            data = ticketRepository.createNewTicket(data,user_id)
            sendMail(
                name=data.user.name,
                code=data.ticket_code,
                date=data.event.date_of_event,
                event_name=data.event.title,
                location=data.event.address,
                subject="Ticket Event",
                to=data.user.email
                )
            
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