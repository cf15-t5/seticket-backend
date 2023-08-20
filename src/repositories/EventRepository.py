from src.models.Event import Event,db
class EventRepository:
  def getAllEvent(self):
    return Event.query.all()  
  def createNewEvent(self,title,description,price,date_of_event,number_of_ticket,user_id,poster_path,address):
    newEvent = Event(
      title=title, 
      description=description,
      price=price,
      date_of_event=date_of_event,
      number_of_ticket=number_of_ticket,
      address=address,
      user_id=user_id,
      poster_path=poster_path
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