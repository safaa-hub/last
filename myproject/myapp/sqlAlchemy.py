from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from .models import User

engine = create_engine("mysql+pymysql://root:Root@localhost/django", echo=True)
engine.connect()

session = scoped_session(sessionmaker(bind=engine))
s = session()

#  print(engine)


def create_user(first_name, last_name, birth_date, gender, user_name, password):
    user = User(first_name, last_name, birth_date, gender, user_name, password)
    s.add(user)
    s.commit()
    s.close()
