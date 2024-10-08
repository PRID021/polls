from django.http import JsonResponse
from rest_framework import status

from .error_definition import error_codes, error_messages, messages


def response_ok(data=None, meta={}):
    result = {"code": status.HTTP_200_OK, "message": messages["success"]}
    if meta:
        result.update({"meta": meta})
    if data is not None:
        result.update({"data": data})
    return JsonResponse(
        result,
        status=status.HTTP_200_OK,
    )


def response_err401(code=None, message=None):
    if code is None:
        code = error_codes["unauthorized"]["common"]
    if message is None:
        message = error_messages["unauthorized"]["common"]
    error = {"code": code, "message": message}
    return JsonResponse(
        error,
        status=status.HTTP_401_UNAUTHORIZED,
    )


def response_err422(errors, code=None, message=None):
    if code is None:
        code = error_codes["unprocessable_entity"]["common"]
    if message is None:
        message = error_messages["unprocessable_entity"]["common"]

    error = {
        "code": code,
        "message": message,
        "errors": errors,
    }
    return JsonResponse(
        error,
        status=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


def response_err400(err=None, code=None):
    if code is None:
        code = status.HTTP_400_BAD_REQUEST
    error = {"code": code, "message": error_messages["bad_request"]["common"]}
    if err:
        error.update(err)
    return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)


def response_err404(code=None, message=None):
    if code is None:
        code = error_codes["not_found"]["common"]
    if message is None:
        message = error_messages["not_found"]["common"]
    error = {"code": code, "message": message}
    return JsonResponse(error, status=status.HTTP_404_NOT_FOUND)
