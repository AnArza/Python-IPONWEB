from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserVerificationCode(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True, )

    verification_code = models.TextField(default='', editable=False)

    @property
    def verification(self):
        print(self.user.username)
        self.verification_code = hash(self.user.username)
        self.save()
        return self.verification_code
