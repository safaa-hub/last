from .models import User
from .models import s
from .serializers import UserSerializer


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
        return user_[0]
    else:
        return None


def is_exist_email(email):
    user_ = s.query(User).filter_by(email=email).all()
    #  print(user_)
    if len(user_) > 0:
        return True
    else:
        return False


def get_user(id):
    user_serializer = UserSerializer()
    user = s.query(User).filter_by(id=id).all()
    if len(user) > 0:
        dump_data = user_serializer.dump(user[0])
        return dump_data
    else:
        return None

