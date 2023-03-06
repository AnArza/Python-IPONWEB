import json

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auth_app.models import UserVerificationCode


@api_view(['POST'])
@permission_classes((AllowAny,))
def verify(request):
    data = json.loads(request.body.decode("utf-8"))
    try:
        email = data['email']
        verification_code = data['verification_code']
    except KeyError:
        return Response("Key Error happened")
    try:
        user_verif = UserVerificationCode.objects.get(user__username=email)
        if user_verif.verification_code == verification_code:
            user_verif.user.is_active = True
            user_verif.user.save()
            return Response("Verified successfully")
    except ObjectDoesNotExist:
        return Response("No such username")
    return Response("Wrong verification code")
