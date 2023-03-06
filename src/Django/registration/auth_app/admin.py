from django.contrib import admin
from .models import UserVerificationCode


# Register your models here.


class UserVerificationCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'verification')


admin.site.register(UserVerificationCode, UserVerificationCodeAdmin)
