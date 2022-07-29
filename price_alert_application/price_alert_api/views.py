from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

import json

from .models import User,Alert

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class Alert_Api(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        a_name = data.get('alert_name')
        a_price = data.get('alert_price')
        a_crypto_currency = data.get('alert_crypto_currency')
        a_status = "created"

        alert_data = {
            'name': a_name,
            'crytoCurrency': a_crypto_currency,
            'price': a_price,
            'status': a_status,
        }

        alert_item = Alert.objects.create(**alert_data)

        data = {
            "message": f"New item added to Cart with id: {alert_item.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        items = Alert.objects.all()
        items_count = Alert.objects.count()

        items_data = []
        for item in items:
            items_data.append({
                'alert_name': item.name,
                'alert_crypto_currency': item.crytoCurrency,
                'alert_price': item.price,
                'alert_status': item.status,
            })

        data = {
            'count': items_count,
            'items': items_data,
        }

        return JsonResponse(data, status=200)


