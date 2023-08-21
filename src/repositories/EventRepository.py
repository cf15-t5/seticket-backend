from src.models.Event import Event,db
from src.models.Category import Category,db
from datetime import datetime
import sys
class EventRepository:
  def getAllEvent(self):
    return Event.query.all()  
  
  def getAllEventFiltered(self,filters):
    
    events = Event.query.all()
    # print('filters',filters)

    filtered_events = [event for event in events if
                       (not filters['province'] or event.address.split(',')[3].strip()== filters['province']) and
                       (not filters['city'] or event.address.split(',')[2].strip() == filters['city']) and
                       (not filters['district'] or event.address.split(',')[1].strip() == filters['district'] ) and
                        (not filters['category'] or str(event.category_id) == filters['category']) and
                        (not filters['date'] or event.date_of_event.date() == datetime.strptime(filters['date'], '%Y-%m-%d').date()) and 
                        (not filters['status'] or event.status == filters['status'])


                       ]
    today = datetime.today().date()
    if(filters['type'] == 'upcoming'):
      filtered_events = [event for event in filtered_events if event.date_of_event.date() >= today]
      
    return filtered_events
  def createNewEvent(self,title,description,price,date_of_event,number_of_ticket,user_id,poster_path,address,category_id):
    newEvent = Event(
      title=title, 
      description=description,
      price=price,
      date_of_event=date_of_event,
      number_of_ticket=number_of_ticket,
      address=address,
      user_id=user_id,
      poster_path=poster_path,
      category_id=category_id
      )
    db.session.add(newEvent)
    db.session.commit()
    return dict(newEvent)
  
  def getEventById(self,event_id):
    return Event.query.filter_by(event_id=event_id).first()
  
  def updateEvent(self,event_id,title,description,price,date_of_event,number_of_tickets,poster_path):
    event = Event.query.filter_by(event_id=event_id).first()
    if(not event) :return False
    event.title = title
    event.description = description
    event.price = price
    event.date_of_event = date_of_event
    event.number_of_ticket = number_of_tickets
    event.poster_path = poster_path
    db.session.commit()
    return dict(event)
  
  def deleteEvent(self,event_id):
    event = Event.query.filter_by(event_id=event_id).first()
    if(not event) :return False
    db.session.delete(event)
    db.session.commit()
    return True
  
  def updateStatus(self,event_id,status):
    event = Event.query.filter_by(event_id=event_id).first()
    if(not event) :return False
    event.status = status
    db.session.commit()
    return dict(event)
  
  def getAllEventByUserId(self,user_id):
    return Event.query.filter_by(user_id=user_id).all()