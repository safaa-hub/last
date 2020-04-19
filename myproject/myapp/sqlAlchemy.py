from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from .models import User, Base

engine = create_engine("mysql+pymysql://root:Root@localhost/django", echo=True)
engine.connect()

session = scoped_session(sessionmaker(bind=engine))
s = session()


#  print(engine)


def create_user(first_name, last_name, birth_date, gender, email, password):
    user = User(first_name=first_name, last_name=last_name, birth_date=birth_date, gender=gender, email=email,
                password=password)

    s.add(user)
    s.commit()
    s.close()


def is_exist(email, password):
    user_ = s.query(User).filter_by(email=email, password=password).all()
    #  print(user_)
    if len(user_) > 0:
        return True
    else:
        return False


def get_user(pk):
    user = s.query(User).filter_by(id=pk).all()
    #  if user:
    #    user_serialized = UserSerializer(user)
    if len(user) > 0:
        return user[0]
