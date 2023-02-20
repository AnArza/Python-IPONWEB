from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json

from market.models import Store, StoreOwner, StoreCategory
from .helper_functions import data_status, ok_status, failed_status


class StoreView(View):

    def get(self, request):
        stores = Store.objects.all()
        data = []
        for store in stores:
            data.append({'id': store.id, 'name': store.name, 'owner': str(store.owner),
                         'store_category': str(store.store_category)})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        if 'owner_id' in data and 'store_category_id' in data and 'name' in data:
            try:
                store = Store.objects.create(
                    name=data['name'],
                    owner=StoreOwner.objects.get(pk=data['owner_id']),
                    store_category=StoreCategory.objects.get(pk=data['store_category_id']),
                )
            except ObjectDoesNotExist:
                return failed_status("No object with that id")
        else:
            return failed_status("invalid_post_data")
        store.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreView.get_by_id(request, id)
        if request.method == "DELETE":
            return StoreView.delete(request, id)
        if request.method == "PATCH":
            return StoreView.edit(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status(
            {'id': store.id, 'name': store.name, 'owner': str(store.owner),
             'store_category': str(store.store_category)})

    @staticmethod
    def delete(request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        store.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if 'owner_id' in data:
            try:
                store.owner = StoreOwner.objects.get(pk=data['owner_id'])
            except ObjectDoesNotExist:
                return failed_status("No object with that id")
        if 'category_id' in data:
            try:
                store.store_category = StoreCategory.objects.get(pk=data['category_id'])
            except ObjectDoesNotExist:
                return failed_status("No object with that id")
        if 'name' in data:
            store.name = data['name']
        store.save()
        return ok_status()
