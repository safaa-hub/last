from ..utils import InvalidType
import datetime


def check_type(function):
    def inner(request, *args, **kwargs):
        if not isinstance(request.data.get("first_name"), str) or not isinstance(request.data.get("last_name"), str) or not isinstance(request.data.get("gender"), str) or not isinstance(request.data.get("password"), str) or not isinstance(request.data.get("user_name"), str):
            raise InvalidType
        elif not isinstance(request.data.get("birth_date"), datetime.date):
            raise InvalidType
        else:
            return function(request, *args, **kwargs)
    return inner
