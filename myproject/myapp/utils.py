from django.http import Http404
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status


def custom_exception_handler(exc, context):
    print("hyneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    global code
    response = exception_handler(exc, context)
    if isinstance(exc, APIException):
        print("ApIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        status_code = exc.status_code
        data = exc.default_detail
        code = exc.default_code

    elif isinstance(exc, Http404):
        print("40000000000000000000000000000000000000000000000000000000004")
        status_code = status.HTTP_404_NOT_FOUND
        data = "Not Found"
        code = 404

    else:
        print("elseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        data = str(exc)
        code = 500

    response.data["status code"] = status_code
    response.data["data"] = data
    response.data["code"] = code

    return response


class InvalidEmail(APIException):
    status_code = status.HTTP_205_RESET_CONTENT
    default_code = 600
    default_detail = "Invalid Email"


class NoContent(APIException):
    status_code = status.HTTP_204_NO_CONTENT
    default_code = 601
    default_detail = "No Content sent"


class IncorrectPassword(APIException):
    status_code = status.HTTP_205_RESET_CONTENT
    default_code = 602
    default_detail = "Incorrect Password"


class NotLoggedIn(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_code = 603
    default_detail = "You're Not Logged In"


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 604
    default_detail = "Bad Request"


class InvalidType(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_code = 605
    default_detail = "Invalid Data Type"
