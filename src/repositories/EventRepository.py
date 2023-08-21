from src.models.Event import Event,db
from src.models.Category import Category,db

class EventRepository:
  def getAllEvent(self):
    return Event.query.all()  
  
  def getAllEventFiltered(self,filters):
    query = Event.query

    if 'address' in filters and filters['address']:
        query = query.filter(Event.address.ilike(f"%{filters['address']}%"))

    if 'date_of_event' in filters and filters['date_of_event']:
        query = query.filter(Event.date_of_event >= filters['date_of_event'])

    if 'category_name' in filters and filters['category_name']:
        query = query.join(Category).filter(Category.name.ilike(f"%{filters['category_name']}%"))

    if 'name' in filters and filters['name']:
        query = query.filter(Event.name.ilike(f"%{filters['name']}%"))

    return query.all()
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