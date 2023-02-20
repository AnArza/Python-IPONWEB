from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json

from django.contrib.auth.models import User
from market.models import Customer
from .helper_functions import data_status, ok_status, failed_status


class CustomerView(View):

    def get(self, request):
        customers = Customer.objects.all()
        data = []
        for customer in customers:
            data.append({'id': customer.id, 'user': str(customer.user), 'registered_at': str(customer.registered_at),
                         'avatar': str(customer.avatar)})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        if 'user_id' in data:
            try:
                customer = Customer.objects.create(
                    user=User.objects.get(pk=data['user_id'])
                )
            except ObjectDoesNotExist:
                return failed_status("No object with that id")
        else:
            return failed_status("invalid_post_data")
        if 'avatar' in data:
            customer.avatar = data['avatar']
        customer.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return CustomerView.get_by_id(request, id)
        if request.method == "DELETE":
            return CustomerView.delete(request, id)
        if request.method == "PATCH":
            return CustomerView.edit(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status(
            {'id': customer.id, 'user': str(customer.user), 'registered_at': str(customer.registered_at),
             'avatar': str(customer.avatar)})

    @staticmethod
    def delete(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        customer.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if 'user_id' in data:
            try:
                customer.user = User.objects.get(pk=data['user_id'])
            except ObjectDoesNotExist:
                return failed_status("No object with that id")
        if 'avatar' in data:
            customer.avatar = data['avatar']
        customer.save()
        return ok_status()
