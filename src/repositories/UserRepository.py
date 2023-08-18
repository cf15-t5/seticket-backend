from src.models.User import User,db
import bcrypt
import sys
class UserRepository:
  def getAllUser(self):
    return User.query.all()  
  
  def getUserByEmail(self,email):
    return User.query.filter_by(email=email).first()
  def createNewUser(self,data):
    print(data,file=sys.stderr) 
    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    newUser = User(
      name=data['name'], 
      email=data['email'],
      password=password,
      status='INACTIVE' if data['role'] == 'EVENT_ORGANIZER' else 'ACTIVE',
      role=data['role'],
      balance=0
      )
    db.session.add(newUser)
    db.session.commit()
    return dict(newUser)
  def getUserById(self,user_id):
    return User.query.filter_by(user_id=user_id).first()