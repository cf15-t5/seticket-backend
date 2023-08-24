
from src.repositories.EventRepository import EventRepository
from src.utils.convert import queryResultToDict
from src.services.Service import Service
from src.utils.uploadFile import upload_file,delete_file
from src.utils.validator.EventValidator import CreateNewEventValidator,UpdateEventValidator,DeleteEventValidator,VerifyEventValidator
import sys
from src.utils.errorHandler import errorHandler
eventRepository = EventRepository()    

class EventService(Service):
    @staticmethod
    def failedOrSuccessRequest(status, code, data):
        return {
            'status': status,
            "code": code,
            'data': data,
        }
    
    def _count_ticket_and_attendace(self,events:list):
        for event in events:
                event['ticket_count'] = len(event['tickets'])
                event['attendances_count'] =  len([ticket for ticket in event['tickets'] if ticket['is_attended']])
                event.pop('tickets')
        return events
    def getAllEvent(self,filter):
        try:
            if( any(value is not None for value in filter.values())):
                data = eventRepository.getAllEventFiltered(filter)
            else:
                data = eventRepository.getAllEvent()
            # add ticket count to each event
            data_dict = queryResultToDict(data,['user','category','tickets'])
            result = self._count_ticket_and_attendace(data_dict)
            
            return EventService.failedOrSuccessRequest('success', 200,result )
        except Exception as e:
            print(e)
            return EventService.failedOrSuccessRequest('failed', 500, str(e))
    def getEventById(self,id):
        try:
            event = eventRepository.getEventById(id)
            if not event:
                return EventService.failedOrSuccessRequest('failed', 404, 'Event not found')
            data_dict = queryResultToDict([event],['user','category'])[0]
            result = self._count_ticket_and_attendace([data_dict])[0]
            return EventService.failedOrSuccessRequest('success', 200, result)
        except Exception as e:
            return EventService.failedOrSuccessRequest('failed', 500, str(e))
        
    def createEvent(self,data,file,user_id):
        try:
            
            validate = CreateNewEventValidator(**data)
            if not validate:
                return EventService.failedOrSuccessRequest('failed', 400, 'Validation failed')
            if not file['poster']:
                return EventService.failedOrSuccessRequest('failed', 400, 'poster is required')
            poster = upload_file(file['poster'])
            newEvent = eventRepository.createNewEvent(**data,poster_path=poster,user_id=user_id)
            return EventService.failedOrSuccessRequest('success', 201, queryResultToDict([newEvent])[0])
        except ValueError as e:
            return EventService.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
        except Exception as e:
              return EventService.failedOrSuccessRequest('failed', 500, str(e))
    def updateEvent(self,id,data,file ,user_id):
        try:
          validate = UpdateEventValidator(**data,id=id)
          if not validate:
              return EventService.failedOrSuccessRequest('failed', 400, 'Validation failed')
          event = eventRepository.getEventById(id)
          if not event:
            return EventService.failedOrSuccessRequest('failed', 404, 'Event not found')
          data_dict = data.to_dict()
          event_copied = queryResultToDict([event])[0]
          
          if file:
            event_copied['poster_path'] = upload_file(file['poster'])
          event_copied.update(data_dict)
          event_copied.pop('user_id')
          event_copied.pop('status')
          
          eventUpdated = eventRepository.updateEvent(**event_copied)
          return EventService.failedOrSuccessRequest('success', 201, queryResultToDict([eventUpdated])[0])
        except ValueError as e:
            return EventService.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
        except Exception as e:
              return EventService.failedOrSuccessRequest('failed', 500, str(e))
    def deleteEvent(self,id):
        try:
          validate = DeleteEventValidator(id=id)
          if(not validate):
            return EventService.failedOrSuccessRequest('failed', 400, 'Validation failed')
          event = eventRepository.getEventById(id)
          if not event:
            return EventService.failedOrSuccessRequest('failed', 404, 'Event not found')
          delete_file(event.poster_path)
          eventRepository.deleteEvent(id)
          return EventService.failedOrSuccessRequest('success', 200, 'Event deleted')
        except ValueError as e:
            return EventService.failedOrSuccessRequest('failed', 500, errorHandler(e.errors()))
        except Exception as e:
              return EventService.failedOrSuccessRequest('failed', 500, str(e))
    def verifyEvent(self,data):
        try:
            
            validate= VerifyEventValidator(**data)
            if(not validate):
                return self.failedOrSuccessRequest('failed',400,'Validation Error')
            eventRepository.updateStatus(event_id=data['id'],status=data['status'])
            return self.failedOrSuccessRequest('sucess',200,"Event Sucess Verified")
        except ValueError as e:
            return self.failedOrSuccessRequest('failed',400,errorHandler(e.errors()))
        except Exception as e:
            return self.failedOrSuccessRequest('failed',400,str(e))
    def getMyEvent(self,user_id):
        try:
            data = eventRepository.getAllEventByUserId(user_id)
            data_dict = queryResultToDict(data,['user','category','tickets'])
            result = self._count_ticket_and_attendace(data_dict)
            
            return EventService.failedOrSuccessRequest('success', 200,result)
        except Exception as e:
            return EventService.failedOrSuccessRequest('failed', 500, str(e))