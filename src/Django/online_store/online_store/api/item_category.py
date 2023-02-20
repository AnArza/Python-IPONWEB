from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
import json

from market.models import ItemCategory
from .helper_functions import data_status, ok_status, failed_status


class ItemCategoryView(View):

    def get(self, request):
        items = ItemCategory.objects.all()
        data = []
        for item in items:
            data.append({'id': item.id, 'name': item.name, 'picture': str(item.picture)})
        return data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        if 'name' in data and 'picture' in data:
            category = ItemCategory.objects.create(
                name=data['name'],
                picture=data['picture']
            )
        elif 'name' in data:
            category = ItemCategory.objects.create(
                name=data['name'],
            )
        elif 'picture' in data:
            category = ItemCategory.objects.create(
                picture=data['picture']
            )
        else:
            return failed_status("invalid_post_data")
        category.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemCategoryView.get_by_id(request, id)
        if request.method == "DELETE":
            return ItemCategoryView.delete(request, id)
        if request.method == "PATCH":
            return ItemCategoryView.edit(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        return data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        category.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return failed_status("obj_not_found")
        if "name" in data:
            category.name = data['name']
        if "picture" in data:
            category.picture = data['picture']
        category.save()
        return ok_status()
