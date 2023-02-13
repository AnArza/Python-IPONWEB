from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotFound
from market.models import StoreCategory, ItemCategory
import json


class StoreCategoryView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({'data': data, 'status': 'ok'}),
            status=200,
            content_type='application/json'
        )

    def get(self, request):
        stores = StoreCategory.objects.all()
        data = []
        for store in stores:
            data.append({'name': store.name, 'picture': str(store.picture)})
        return StoreCategoryView.data_status(data)

    def post(self, request):
        data = json.loads(request.body)
        category = StoreCategory.objects.create(
            name=data['name']
        )
        category.save()
        return self.ok_status()

    @staticmethod
    def ok_status():
        return HttpResponse(
            json.dumps({"status": "ok"}), status=200, content_type="application/json"
        )

    @staticmethod
    def failed_status(status):
        return HttpResponse(
            json.dumps({"status": status}), status=404, content_type="application/json"
        )

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreCategoryView.get_by_id(request, id)
        if request.method == "DELETE":
            return StoreCategoryView.delete(request, id)
        if request.method == "PATCH":
            return StoreCategoryView.edit(request, id)

    @staticmethod
    def get_by_id(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return StoreCategoryView.failed_status("obj_not_found")
        return StoreCategoryView.data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        category.delete()
        return StoreCategoryView.ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        category.save()
        return StoreCategoryView.ok_status()
