from sqlalchemy import Column, Integer, String, ForeignKey
from test.create_order import create_db
from test.create_order import base


class Orders(base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    time = Column(Integer)
    date = Column(String)
    food = Column(String)


    def __init__(self, time, date, food):
        self.time = time
        self.date = date
        self.food = food

create_db()
