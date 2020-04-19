from rest_framework import status, viewsets
from .sqlAlchemy import create_user, is_exist, get_user
from rest_framework.response import Response
from rest_framework import viewsets


class RegisterViewSet(viewsets.ViewSet):
    #  @api_view(['POST'])
    #  @action(detail=True, methods=['post'])
    def create(self, request):
        data = request.data
        if data:
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            birth_date = request.data.get('birth_date')
            gender = request.data.get('gender')
            email = request.data.get('email')
            password = request.data.get('password')
            k = is_exist(email, password)
            if k is True:
                return Response(status=status.HTTP_306_RESERVED)
            else:
                create_user(first_name, last_name, birth_date, gender, email, password)
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(viewsets.ViewSet):

    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        v = is_exist(email, password)
        if v:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class GetUser(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        user = get_user(pk)
        return Response(user, status=status.HTTP_202_ACCEPTED)
