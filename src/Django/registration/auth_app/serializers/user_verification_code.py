from rest_framework import serializers

from ..models import UserVerificationCode


class UserVerificationCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserVerificationCode
        fields = ['user', 'verification_code']
