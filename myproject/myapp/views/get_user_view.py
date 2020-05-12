from django.http import Http404
from rest_framework import status
from ..repositories.user_repository import UserRepository
from rest_framework.response import Response
from rest_framework import viewsets
from ..utils import NotLoggedIn, BadRequest
#  from ..decorators.login_required import user_login_required

user_repository = UserRepository()


class GetUser(viewsets.ViewSet):
    def retrieve(self, request, pk):
        if pk:
            user = user_repository.get_user_info(pk)
            if user is None:
                raise Http404
            else:
                if request.session.get('user_id') == user.get("id"):
                    return Response(user, status=status.HTTP_200_OK)
                else:
                    raise NotLoggedIn
        else:
            raise BadRequest
