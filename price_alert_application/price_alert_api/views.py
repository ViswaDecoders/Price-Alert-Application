from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

import json
import jwt
import datetime

from .models import User,Alert

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

secretkey = 'SeCrEtKeY'

@method_decorator(csrf_exempt, name='dispatch')
class User_Create(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        u_name = data.get('user_name')
        
        if len(User.objects.filter(name=u_name)) == 1:
            data = {
                "message": f"User already Exists with the name {u_name}",
            }
            return JsonResponse(data, status=400)
        else:
            user_data = {
                'name': u_name,
            }
            user = User.objects.create(**user_data)

            data = {
                "message": f"New user created with id: {user.id}",
            }
            return JsonResponse(data, status=201)
    
@method_decorator(csrf_exempt, name='dispatch')
class User_Login(APIView):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        u_name = data.get('user_name')

        try:
            user = User.objects.get(name=u_name)
        except:
            user = None
        
        if user is None:
            raise AuthenticationFailed("User Not Found")
        
        payload = {
            'name': u_name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, secretkey, algorithm='HS256')

        user.authCode = token
        user.save()

        response = Response()
        response.set_cookie(key='authToken',value=token, httponly=True)
        response.data = {
            "message": f"User Logged Succefully of id: {user.id}",
            "authToken": f"{token}"
        }
        return response


class User_Logout(APIView):
    def get(self, request):
        response = Response()
        response.delete_cookie('authtoken')
        response.data = {
            "message": "Logout Success"
        }
        return response

@method_decorator(csrf_exempt, name='dispatch')
class Alert_Api(View):
    def post(self, request):
        ctoken = request.COOKIES.get('authtoken')
        htoken = request.headers['Authorization'].split()[1]

        if not ctoken and not htoken:
            return JsonResponse({"message": f"Token Missing",}, status=401)
        
        token=ctoken=htoken
        try:
            payload = jwt.decode(token, secretkey, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return JsonResponse({"message": f"Token Expired, Kindly Relogin",}, status=401)
        except:
            return JsonResponse({"message": f"Invalid Token",}, status=401)
        
        user = User.objects.get(name=payload['name'])    
        data = json.loads(request.body.decode("utf-8"))
        a_name = data.get('alert_name')
        a_price = data.get('alert_price')
        a_crypto_currency = data.get('alert_crypto_currency')
        a_status = "created"

        alert_data = {
            'user': user.name,
            'name': a_name,
            'crytoCurrency': a_crypto_currency,
            'price': a_price,
            'status': a_status
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

