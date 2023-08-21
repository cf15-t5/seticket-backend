
from src.repositories.TicketRepository import TicketRepository
from src.utils.convert import queryResultToDict
from src.services.Service import Service
from src.utils.validator.TicketValidator import CreateNewTicketValidator
from src.utils.errorHandler import errorHandler
from src.utils.sendMail import sendMail

ticketRepository = TicketRepository()    

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
            
            return self.failedOrSuccessRequest('success', 200, data.serialize())
        except ValueError as e:
          return self.failedOrSuccessRequest('failed', 400, errorHandler(e.errors()))
        except Exception as e:
            return self.failedOrSuccessRequest('failed', 500, str(e))