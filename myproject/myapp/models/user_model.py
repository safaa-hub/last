<<<<<<< HEAD:myproject/myapp/models/user_model.py
from sqlalchemy import Column, Integer, String, Date
from ..common_file import Base, engine


class User(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', birth_date='%s' , gender='%s')>" % (
            self.first_name, self.last_name, self.birth_date, self.gender)


Base.metadata.create_all(engine)
=======
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("mysql+pymysql://root:Root@localhost/django", echo=True)
session = scoped_session(sessionmaker(bind=engine))
engine.connect()
s = session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(first_name='%s', last_name='%s', birth_date='%s' , gender='%s')>" % (
            self.first_name, self.last_name, self.birth_date, self.gender)


Base.metadata.create_all(engine)
>>>>>>> 002e0fea01e9e0adfba9b57106f62e2ad9467f5d:myproject/myapp/models.py
