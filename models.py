from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from app import db


class Items(db.Model):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    label_one = Column(String)
    label_two = Column(String)
    label_three = Column(String)
    label_four = Column(String)

db.create_all()