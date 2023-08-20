from src.server.main import db,main_app
from src.config.database import generateDatabase
class Category(db.Model):
  __tablename__ = 'categories'
  
  category_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), unique=True)
  
  def __init__(self,name ):
    self.name = name
  
  def __repr__(self):

    return f"<Event (id={self.event_id}, name={self.name})>"
  
  
  def toDict(self):
      return {
          'category_id': self.category_id,
          'name': self.name,
      }
      
  def __iter__(self):
      yield 'category_id', self.category_id
      yield 'name', self.name
    