from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine("mysql+pymysql://root:Root@localhost/django", echo=True)
session = scoped_session(sessionmaker(bind=engine))
engine.connect()
Session = session()

Base = declarative_base()
