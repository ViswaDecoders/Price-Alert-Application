from rest_framework import serializers

from price_alert_api.models import Alert, User

class AlertSerializer(serializers.ModelSerializer):
   class Meta:
       model = Alert
       fields = ('user', 'name', 'crytoCurrency', 'price', 'status')


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('name')