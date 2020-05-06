from .models import User
from .common_file import s
from .serializers import UserSerializer
import hashlib
from .constant_file import SALT


def create_user(first_name, last_name, birth_date, gender, email, password):
    encoded_password = hashlib.md5((str(password) + SALT).encode('utf-8')).hexdigest()
    user = User(first_name=first_name, last_name=last_name, birth_date=birth_date, gender=gender, email=email,
                password=encoded_password)

    s.add(user)
    s.commit()
    s.close()


def get_user_by_email(email):
    user_ = s.query(User).filter_by(email=email).all()
    #  print(user_)
    if len(user_) > 0:
        return user_[0]
    else:
        return None


def get_user_info(id):
    user_serializer = UserSerializer()
    user = s.query(User).filter_by(id=id).all()
    if len(user) > 0:
        dump_data = user_serializer.dump(user[0])
        return dump_data
    else:
        return None

