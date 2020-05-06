from django.http import Http404
from rest_framework import status
from rest_framework.status import HTTP_404_NOT_FOUND

from .sqlAlchemy import create_user, get_user_by_email, get_user_info
from rest_framework.response import Response
from rest_framework import viewsets
import hashlib
from .constant_file import SALT
from .utils import InvalidEmail, NoContent, IncorrectPassword, NotLoggedIn, BadRequest


class RegisterViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        if data:
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            birth_date = request.data.get('birth_date')
            gender = request.data.get('gender')
            email = request.data.get('email')
            password = request.data.get('password')
            if get_user_by_email(email) is None:
                create_user(first_name, last_name, birth_date, gender, email, password)
                return Response("Created", status=status.HTTP_201_CREATED)
            else:
                raise InvalidEmail
        else:
            raise NoContent


class LoginView(viewsets.ViewSet):

    def create(self, request):
        data = request.data
        if data:
            email = request.data.get("email")
            password = request.data.get("password")
            user = get_user_by_email(email)
            if user is None:
                raise InvalidEmail
            else:
                encoded_password = hashlib.md5((str(password) + SALT).encode('utf-8')).hexdigest()
                if user.password == encoded_password:
                    request.session['user_id'] = user.id
                    return Response("logged in Successfully", status=status.HTTP_200_OK)
                else:
                    raise IncorrectPassword
        else:
            raise NoContent


class GetUser(viewsets.ViewSet):
    def retrieve(self, request, pk):
        if pk:
            user = get_user_info(pk)
            if user is None:
                raise Http404
            else:
                if request.session.get('user_id') == user.get("id"):
                    return Response(user, status=status.HTTP_200_OK)
                else:
                    raise NotLoggedIn
        else:
            raise BadRequest
