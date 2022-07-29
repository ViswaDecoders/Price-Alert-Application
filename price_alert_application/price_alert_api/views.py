from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

import json

from .models import User,Alert

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class AlertAdd(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        a_name = data.get('alert_name')
        a_price = data.get('alert_price')
        a_status = "created"

        alert_data = {
            'name': a_name,
            'price': a_price,
            'status': a_status,
        }

        alert_item = Alert.objects.create(**alert_data)

        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }
        return JsonResponse(data, status=201)


