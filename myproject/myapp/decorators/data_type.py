import time

from ..utils import InvalidFirstName, InvalidPassword, InvalidLastName, InvalidGender, InvalidBirthDate


def check_type(function):
    def inner(request, *args, **kwargs):
        try:
            request = request.request
            birth_date = request.data.get('birth_date')
            result = time.strptime(birth_date, '%Y-%m-%d')
            if not isinstance(request.data.get("first_name"), str):
                raise InvalidFirstName
            elif not isinstance(request.data.get("last_name"), str):
                raise InvalidLastName
            elif not isinstance(request.data.get("gender"), str):
                raise InvalidGender
            elif not isinstance(request.data.get("password"), str):
                raise InvalidPassword
            elif type(result) is not time.struct_time:
                raise InvalidBirthDate
            else:
                return function(request, *args, **kwargs)
        except:
            raise InvalidBirthDate

    return inner
