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
  status_change_at = db.Column(db.DateTime, nullable=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
  category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'))
  category = db.relationship('Category', backref='events')
  user = db.relationship('User', backref='events')
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
  