import bcrypt
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from base import BaseModel

Base = declarative_base()

class User(Base, BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(20), nullable=False, unique=True)
    pwhash = Column(String(60), nullable=False)
    email = Column(String(140), nullable=False, unique=True)

"""
Object that handles SQL calls to the user table
"""
class UserManager():

    def create_user(self, session, username, email, password):
        pwhash = bcrypt.hashpw(password, bcrypt.gensalt(14))
        new_user = User(username=username, email=email, pwhash=pwhash)
        session.add(new_user)
        session.commit()
        return new_user

    def get_user(self, session, query):
        return session.query(User).filter_by(**query).first()

    def get_users(self, session):
        return session.query(User)

    def delete_user(self, session, user):
        session.delete(user)
        session.commit()
