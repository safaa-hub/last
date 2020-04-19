from .models import User
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class UserSerializer(SQLAlchemySchema):
    class Meta:
        Model = User
        load_instance = True
    #  fields = '__all__'
    id = auto_field()
    first_name = auto_field()
    last_name = auto_field()
    birth_date = auto_field()
    gender = auto_field()
    email = auto_field()
    password = auto_field()
