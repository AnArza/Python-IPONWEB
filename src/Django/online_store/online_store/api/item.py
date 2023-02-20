from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json

from market.models import Item, Store, ItemCategory
from .helper_functions import data_status, ok_status, failed_status


class ItemView(View):

    def get(self, request):
        items = Item.objects.all()
        data = []
        for item in items:
            data.append({'id': item.id, 'name': item.name, 'picture': str(item.picture),
                         'price': str(item.price), 'quantity': item.quantity, 'info': item.info,
                         'store': str(item.store), 'category': str(item.category)})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        if 'price' in data and 'quantity' in data and 'name' in data and 'store_id' in data and 'category_id' in data:
            try:
                item = Item.objects.create(
                    name=data['name'],
                    store=Store.objects.get(pk=data['store_id']),
                    quantity=data['quantity'],
                    category=ItemCategory.objects.get(pk=data['category_id']),
                    price=data['price']
                )
            except ObjectDoesNotExist:
                return failed_status("No object with that id")
        else:
            return failed_status("invalid_post_data")
        if 'picture' in data:
            item.picture = data['picture']
        if 'info' in data:
            item.info = data['info']
        item.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemView.get_by_id(request, id)
        if request.method == "DELETE":
            return ItemView.delete(request, id)
        if request.method == "PATCH":
            return ItemView.edit(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status(
            {'id': item.id, 'name': item.name, 'picture': str(item.picture),
             'price': str(item.price), 'quantity': item.quantity, 'info': item.info,
             'store': str(item.store), 'category': str(item.category)})

    @staticmethod
    def delete(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        item.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if 'name' in data:
            item.name = data['name']
        if 'store_id' in data:
            try:
                item.store = Store.objects.get(pk=data['store_id'])
            except ObjectDoesNotExist:
                return failed_status("No object with that id")
        if 'quantity' in data:
            item.quantity = data['quantity']
        if 'category_id' in data:
            try:
                item.category = ItemCategory.objects.get(pk=data['category_id'])
            except:
                return failed_status("No object with that id")
        if 'price' in data:
            item.price = data['price']
        if 'info' in data:
            item.info = data['info']
        if 'picture' in data:
            item.picture = data['picture']
        item.save()
        return ok_status()
