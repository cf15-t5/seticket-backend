from src.server.main import db,main_app
from src.config.database import generateDatabase
class Ticket(db.Model):
  __tablename__ = 'tickets'
  
  ticket_id = db.Column(db.Integer, primary_key=True)
  event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
  ticket_code = db.Column(db.String(6))
  is_attended = db.Column(db.Boolean, default=False)
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  event = db.relationship("Event", backref="tickets")
  user = db.relationship("User", back_populates="tickets")  
  transactions = db.relationship("Transaction", back_populates="ticket")
  def __init__(self, event_id, user_id, ticket_code):
    self.event_id = event_id
    self.user_id = user_id
    self.ticket_code = ticket_code
    