"""""
from ..models.user_model import User
from django.shortcuts import redirect


def user_login_required(function):
    def inner(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return
        else:
            return function(request, *args, **kwargs)
    return inner
"""""