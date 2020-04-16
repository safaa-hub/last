from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from .sqlAlchemy import create_user
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import viewsets


class RegisterViewSet(viewsets.ViewSet):
    #  @api_view(['POST'])
    #  @action(detail=True, methods=['post'])
    def create(self, request):
        data = request.data
        if data is not None:
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            birth_date = request.data.get('birth_date')
            gender = request.data.get('gender')
            user_name = request.data.get('user_name')
            password = request.data.get('password')
            create_user(first_name, last_name, birth_date, gender, user_name, password)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(viewsets.ViewSet):

    def login_fun(self, request):
        user_name = request.get['user_name']
        password = request.get['password']
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
