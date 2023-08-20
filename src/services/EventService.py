
from src.repositories.EventRepository import EventRepository
from src.utils.convert import transformToDictList
from src.services.Service import Service
from src.utils.uploadFile import upload_file,delete_file
from src.utils.validator.EventValidator import CreateNewEventValidator,UpdateEventValidator,DeleteEventValidator

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
    
    def getAllEvent(self):
        try:
            data = eventRepository.getAllEvent()
            print(data)
            return EventService.failedOrSuccessRequest('success', 200, transformToDictList(data))
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
            return EventService.failedOrSuccessRequest('success', 201, newEvent)
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
          event_copied = event.toDict().copy()
          
          if file:
            delete_file(event['poster_path'])
            event_copied['poster_path'] = upload_file(file['poster'])
          event_copied.update(data_dict)
          event_copied.pop('user_id')
          event_copied.pop('status')
          
          print('event',event_copied)
          
          eventUpdated = eventRepository.updateEvent(**event_copied)
          return EventService.failedOrSuccessRequest('success', 201, eventUpdated)
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