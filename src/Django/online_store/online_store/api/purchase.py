from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json

from market.models import Purchase, Item, Customer
from .helper_functions import data_status, ok_status, failed_status


class PurchaseView(View):

    def get(self, request):
        purchases = Purchase.objects.all()
        data = []
        for purchase in purchases:
            data.append({'id': purchase.id, 'items': str(purchase.items.all()),
                         'customer': str(purchase.customer),
                         'buy_time': str(purchase.buy_time),
                         'total_price': purchase.total_price})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        if 'item_ids' in data and 'customer_id' in data:
            try:
                items = Item.objects.filter(id__in=data['item_ids'])
                if len(data['item_ids']) == len(items):
                    purchase = Purchase.objects.create(
                        customer=Customer.objects.get(pk=data['customer_id'])
                    )
                    for item in items:
                        if item.quantity > 0:
                            purchase.items.add(item)
                            item.quantity -= 1
                            item.save()
                        else:
                            purchase.delete()
                            return failed_status("No that much items")
                else:
                    return failed_status("No object with that id")
            except ObjectDoesNotExist:
                return failed_status("No object with that id")
        else:
            return failed_status("invalid_post_data")
        purchase.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return PurchaseView.get_by_id(request, id)
        if request.method == "DELETE":
            return PurchaseView.delete(request, id)
        if request.method == "PATCH":
            return PurchaseView.edit(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status({'id': purchase.id, 'items': str(purchase.items.all()),
                            'customer': str(purchase.customer),
                            'buy_time': str(purchase.buy_time),
                            'total_price': purchase.total_price})

    @staticmethod
    def delete(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        purchase.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if "customer_id" in data:
            purchase.customer = Customer.objects.get(pk=data['customer_id'])
        if "item_ids" in data:
            items = Item.objects.filter(id__in=data['item_ids'])
            if len(data['item_ids']) == len(items):
                saved_items = list(purchase.items.all())
                purchase.items.clear()
                for item in items:
                    if item.quantity > 0:
                        purchase.items.add(item)
                        item.quantity -= 1
                        item.save()
                    else:
                        for it in saved_items:
                            purchase.items.add(it)
                        item.save()
                        return failed_status("No that much items")
            else:
                return failed_status("No object with that id")
        purchase.save()
        return ok_status()
