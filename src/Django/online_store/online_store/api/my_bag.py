from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json

from market.models import MyBag, Item, Customer
from .helper_functions import data_status, ok_status, failed_status


class MyBagView(View):

    def get(self, request):
        my_bags = MyBag.objects.all()
        data = []
        for my_bag in my_bags:
            data.append({'id': my_bag.id, 'items': str(my_bag.items.all()),
                         'customer': str(my_bag.customer),
                         'total_price': my_bag.total_price})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        if 'item_ids' in data and 'customer_id' in data:
            try:
                items = Item.objects.filter(id__in=data['item_ids'])
                if len(data['item_ids']) == len(items):
                    my_bag = MyBag.objects.create(
                        customer=Customer.objects.get(pk=data['customer_id'])
                    )
                    for item in items:
                        my_bag.items.add(item)
                else:
                    return failed_status("No object with that id")
            except ObjectDoesNotExist:
                return failed_status("No object with that id")
        else:
            return failed_status("invalid_post_data")
        my_bag.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return MyBagView.get_by_id(request, id)
        if request.method == "DELETE":
            return MyBagView.delete(request, id)
        if request.method == "PATCH":
            return MyBagView.edit(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            my_bag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status({'id': my_bag.id, 'items': str(my_bag.items.all()),
                            'customer': str(my_bag.customer),
                            'total_price': my_bag.total_price})

    @staticmethod
    def delete(request, id):
        try:
            my_bag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        my_bag.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            my_bag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if "customer_id" in data:
            my_bag.customer = Customer.objects.get(pk=data['customer'])
        if "item_ids" in data:
            items = Item.objects.filter(id__in=data['item_ids'])
            if len(data['item_ids']) == len(items):
                my_bag.items.clear()
                for item in items:
                    my_bag.items.add(item)
            else:
                return failed_status("No object with that id")
        my_bag.save()
        return ok_status()
