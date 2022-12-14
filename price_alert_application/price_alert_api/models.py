from django.db import models

class Alert(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    crytoCurrency = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    authCode = models.TextField()
