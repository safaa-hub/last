from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from .models import User, Base

engine = create_engine("mysql+pymysql://root:Root@localhost/django", echo=True)
engine.connect()

session = scoped_session(sessionmaker(bind=engine))
s = session()

#  print(engine)


def create_user(first_name, last_name, birth_date, gender, user_name, password):
    user = User(first_name=first_name, last_name=last_name, birth_date=birth_date, gender=gender, user_name=user_name,
                password=password)

    s.add(user)
    s.commit()
    s.close()


#  Base.metadata.create_all(engine)
