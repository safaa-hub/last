from rest_framework import status
from ..repositories.user_repository import UserRepository
from rest_framework.response import Response
from rest_framework import viewsets
from ..utils import InvalidEmail, NoContent

user_repository = UserRepository()


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
            if user_repository.get_user_by_email(email) is None:
                user_repository.create_user(first_name, last_name, birth_date, gender, email, password)
                return Response("Created", status=status.HTTP_201_CREATED)
            else:
                raise InvalidEmail
        else:
            raise NoContent
