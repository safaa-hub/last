from rest_framework import status
from .sqlAlchemy import create_user, get_user, is_exist_email, get_password
from rest_framework.response import Response
from rest_framework import viewsets
import hashlib


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
            if is_exist_email(email) is None:
                create_user(first_name, last_name, birth_date, gender, email, password)
                return Response("Created", status=status.HTTP_201_CREATED)
            else:
                return Response("Invalid email", status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response("No Content", status=status.HTTP_204_NO_CONTENT)


class LoginView(viewsets.ViewSet):

    def create(self, request):
        data = request.data
        if data:
            email = request.data.get("email")
            password = request.data.get("password")
            user = is_exist_email(email)
            if user is None:
                return Response("invalid email", status=status.HTTP_401_UNAUTHORIZED)
            else:
                stored_password = get_password(user.email)
                salt = 'N69s5v'
                encoded_password = hashlib.md5((str(password) + salt).encode('utf-8')).hexdigest()
                if stored_password == encoded_password:
                    request.session['user_id'] = user.id
                    return Response("logged in", status=status.HTTP_200_OK)
                else:
                    return Response("incorrect password", status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response("No Content", status=status.HTTP_204_NO_CONTENT)


class GetUser(viewsets.ViewSet):
    def retrieve(self, request, pk):
        if pk:
            user = get_user(pk)
            if user is None:
                return Response("Not Found", status=status.HTTP_404_NOT_FOUND)
            else:
                if request.session.get('user_id') == user.get("id"):
                    return Response(user, status=status.HTTP_200_OK)
                else:
                    return Response("You're not logged in")
        else:
            return Response("Bad Request ", status=status.HTTP_400_BAD_REQUEST)
