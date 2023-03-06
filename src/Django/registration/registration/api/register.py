from __future__ import absolute_import

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import json
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import AllowAny

from auth_app.models import UserVerificationCode
from ..tasks.task import sleep_task

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    sleep_task.delay()
    data = json.loads(request.body)
    try:
        password = data['password']
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
    except KeyError:
        return HttpResponse("Key Error happened")
    if User.objects.filter(username=data['email']).exists():
        return HttpResponse(
            json.dumps(
                {
                    "status": "error",
                    "error": {
                        "code": 1,
                        "text": "The user with that email exists"
                    },
                }
            ),
            status=200,
            content_type="application/json",
        )

    user = User.objects.create_user(username=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.is_active = False
    user.save()
    user_verif = UserVerificationCode(user=user)
    user_verif.save()
    send_confirmation_email(user_verif)

    return Response({"status": "registered"})


def send_confirmation_email(user_verif):
    send_mail(
        subject='Confirmation Email',
        message=strip_tags(render_to_string("mail.html", {"first_name": user_verif.user.first_name,
                                                          "verification_code": user_verif.verification})),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_verif.user.username])

    return Response({"status": "sent email"})
