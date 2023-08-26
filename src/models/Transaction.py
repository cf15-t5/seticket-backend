from src.server.main import db,main_app
from src.config.database import generateDatabase
class Transaction(db.Model):
  __tablename__ = 'transactions'
  
  transaction_id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String(10), nullable=False)
  nominal = db.Column(db.Integer, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
  ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.ticket_id',ondelete='CASCADE'))
  created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
  user = db.relationship("User", back_populates="transactions")  
  ticket = db.relationship("Ticket", back_populates="transactions", cascade="all, delete")
  def __init__(self, type, user_id, nominal):
    self.type = type
    self.user_id = user_id
    self.nominal = nominal
  
  def setTIcketId(self,ticket_id):
    self.ticket_id = ticket_id