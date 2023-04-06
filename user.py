from sqlalchemy import Column, Integer, String, ForeignKey
from flask_login import UserMixin
from test.db_model import base


class User(base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    age = Column(Integer)
    password = Column(String)



    def __init__(self, email, username, password,age):
        self.email = email
        self.username = username
        self.password = password
        self.age = age
