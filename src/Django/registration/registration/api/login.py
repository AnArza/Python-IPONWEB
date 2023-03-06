from django.contrib.auth import authenticate
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
@permission_classes((~IsAuthenticated,))
def login(request):
    data = json.loads(request.body.decode("utf-8"))
    try:
        password = data['password']
        email = data['email']
    except KeyError:
        return Response("Key Error happened")
    user = authenticate(username=email, password=password)
    if user:
        token = RefreshToken.for_user(user)
        return Response({'status': 'logged in', 'access': str(token.access_token), 'refresh': str(token)})
    return Response("Invalid credentials or not verified user")
