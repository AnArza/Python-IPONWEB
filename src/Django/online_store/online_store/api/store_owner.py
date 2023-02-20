from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json

from django.contrib.auth.models import User
from market.models import StoreOwner
from .helper_functions import data_status, ok_status, failed_status


class StoreOwnerView(View):

    def get(self, request):
        store_owners = StoreOwner.objects.all()
        data = []
        for store_owner in store_owners:
            data.append(
                {'id': store_owner.id, 'user': str(store_owner.user), 'registered_at': str(store_owner.registered_at),
                 'avatar': str(store_owner.avatar)})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        if 'user_id' in data:
            try:
                store_owner = StoreOwner.objects.create(
                    user=User.objects.get(pk=data['user_id'])
                )
            except ObjectDoesNotExist:
                return failed_status("No object with that id")
        else:
            return failed_status("invalid_post_data")
        if 'avatar' in data:
            store_owner.avatar = data['avatar']
        store_owner.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwnerView.get_by_id(request, id)
        if request.method == "DELETE":
            return StoreOwnerView.delete(request, id)
        if request.method == "PATCH":
            return StoreOwnerView.edit(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            store_owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status(
            {'id': store_owner.id, 'user': str(store_owner.user), 'registered_at': str(store_owner.registered_at),
             'avatar': str(store_owner.avatar)})

    @staticmethod
    def delete(request, id):
        try:
            store_owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        store_owner.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            store_owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if 'user_id' in data:
            store_owner.user = User.objects.get(pk=data['user_id'])
        if 'avatar' in data:
            store_owner.avatar = data['avatar']
        store_owner.save()
        return ok_status()
