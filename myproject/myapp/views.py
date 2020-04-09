from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .sqlAlchemy import create_user
from rest_framework.response import Response


class RegisterView(APIView):
    @api_view(['POST'])
    def create_new(self, request):
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
