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
        data = request.DATA
        if data is not None:

            first_name = request.DATA.get('first_name')
            last_name = request.DATA.get('last_name')
            birth_date = request.DATA.get('birth_date')
            gender = request.DATA.get('gender')
            user_name = request.DATA.get('user_name')
            password = request.DATA.get('password')
            create_user(first_name, last_name, birth_date, gender, user_name, password)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


"""""
class LoginView(APIView):
    @api_view(['POST'])
    def login_fun(self, request):
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
"""""