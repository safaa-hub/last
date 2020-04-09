from django.db import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    user_name = Column(String)
    password = Column(Integer)

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', birth_date='%s' , gender='%s')>" % (
            self.first_name, self.last_name, self.birth_date, self.gender)

#  Base.metadata.create_all(engine)

