import json

from django.http import HttpResponse


def data_status(data):
    return HttpResponse(
        json.dumps({'data': data, 'status': 'ok'}),
        status=200,
        content_type='application/json'
    )


def ok_status():
    return HttpResponse(
        json.dumps({"status": "ok"}), status=200, content_type="application/json"
    )


def failed_status(status):
    return HttpResponse(
        json.dumps({"status": status}), status=404, content_type="application/json"
    )
