from src.server.main import db,main_app
from src.config.database import generateDatabase
class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    role = db.Column(db.String(255), default='USER')
    password = db.Column(db.String(255))
    balance = db.Column(db.Float, default=0)
    status = db.Column(db.String(255), default='INACTIVE')
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    tickets = db.relationship('Ticket', back_populates='user')
    transactions = db.relationship('Transaction', back_populates='user')
    def __init__(self, email, name, role, password,  status, balance =0):
        self.name = name
        self.email = email
        self.role = role
        self.password = password
        self.balance = balance
        self.status = status
        self.created_at = db.func.now()
        self.updated_at = db.func.now()
    # def __repr__(self):
        # return '<User %r>' % self.name
  