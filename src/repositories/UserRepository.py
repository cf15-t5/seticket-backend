from src.models.User import User, db
import bcrypt
import sys


class UserRepository:

    def getAllUser(self):
        return User.query.all()
    def getUserByRole(self,role):
        return User.query.filter_by(role=role).all()
    
    def getUserByEmail(self, email):
        return User.query.filter_by(email=email).first()

    def createNewUser(self, data):
        password = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
        newUser = User(
            name=data["name"],
            email=data["email"],
            password=password,
            status="INACTIVE" if data["role"] == "EVENT_ORGANIZER" else "ACTIVE",
            role=data["role"],
            balance=0,
        )
        db.session.add(newUser)
        db.session.commit()
        return newUser

    def getUserById(self, user_id):
        return User.query.filter_by(user_id=user_id).first()

    def verifyUser(self, user_id, status):
        user = User.query.filter_by(user_id=user_id).first()
        if not user:
            return False
        user.status = status
        db.session.commit()
        return user

    def updateProfile(self, id, data):
        user = User.query.filter_by(user_id=id).first()
        if not user:
            return False
        user.name = data["name"] or user.name
        user.email = data["email"] or user.email
        user.password = (
            bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
            if data["password"]
            else user.password
        )
        db.session.commit()
        return user

    def updateBalance(self, id, nominal, operator):
        user = User.query.filter_by(user_id=id).first()
        if not user:
            return False
        if operator == "plus":
            user.balance += nominal
        if operator == "minus":
            user.balance -= nominal

        db.session.commit()
        return user

