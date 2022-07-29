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
        alerts = Alert.objects.all()
        alerts_count = Alert.objects.count()

        alerts_data = []
        for alert in alerts:
            alerts_data.append({
                'alert_id': alert.id,
                'alert_name': alert.name,
                'alert_crypto_currency': alert.crytoCurrency,
                'alert_price': alert.price,
                'alert_status': alert.status,
            })

        data = {
            'count': alerts_count,
            'items': alerts_data,
        }

        return JsonResponse(data, status=200)
    
    def patch(self, request, item_id):
        alert = Alert.objects.get(id=item_id)
        alert.status = "deleted"
        alert.save()

        data = {
            'message': f'Item {item_id} has been deleted'
        }

        return JsonResponse(data)

