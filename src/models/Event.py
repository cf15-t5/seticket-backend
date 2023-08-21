from src.server.main import db,main_app
from src.config.database import generateDatabase
class Event(db.Model):
  __tablename__ = 'events'
  
  event_id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), unique=True)
  date_of_event = db.Column(db.DateTime )
  price = db.Column(db.Integer)
  status = db.Column(db.String(255), default='PENDING')
  number_of_ticket = db.Column(db.Integer, default=0)
  description= db.Column(db.Text)
  poster_path = db.Column(db.Text)
  address= db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
  category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
  
  
  def __init__(self, title, description, price, date_of_event, number_of_ticket,user_id,poster_path,address,category_id ):
    self.title= title
    self.description = description
    self.price = price
    self.date_of_event = date_of_event
    self.number_of_ticket = number_of_ticket
    self.user_id = user_id
    self.poster_path = poster_path
    self.status = 'PENDING'
    self.category_id = category_id
    self.address = address
  
  def __repr__(self):

    return f"<Event (id={self.event_id}, title={self.title}, description={self.description}, price={self.price}, date_of_event={self.date_of_event}, number_of_tickets={self.number_of_ticket}, user_id={self.user_id}, poster_path={self.poster_path}, status={self.status},category_id={self.category_id})>"
  
  
  def toDict(self):
      return {
          'event_id': self.event_id,
          'title': self.title,
          'description': self.description,
          'price': self.price,
          'date_of_event': self.date_of_event,
          'number_of_tickets': self.number_of_ticket,
          'user_id': self.user_id,
          'poster_path': self.poster_path,
          'status': self.status,
          'category_id': self.category_id,
      }
      
  def __iter__(self):
      yield 'event_id', self.event_id
      yield 'title', self.title
      yield 'description', self.description
      yield 'price', self.price
      yield 'date_of_event', self.date_of_event
      yield 'number_of_ticket', self.number_of_ticket
      yield 'user_id', self.user_id
      yield 'poster_path', self.poster_path
      yield 'status', self.status
      yield 'category_id', self.category_id
      yield 'address', self.address