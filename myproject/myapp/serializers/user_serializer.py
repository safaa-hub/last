from ..models.user_model import User
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class UserSerializer(SQLAlchemySchema):
    class Meta:
        Model = User
        load_instance = True
    #  fields = '__all__'
    id = auto_field(column_name="id", model=User)
    first_name = auto_field(column_name="first_name", model=User)
    last_name = auto_field(column_name="last_name", model=User)
    birth_date = auto_field(column_name="birth_date", model=User)
    gender = auto_field(column_name="gender", model=User)
    email = auto_field(column_name="email", model=User)

