from django.db import models

class Alert(models.Model):
   name = models.CharField(max_length=100)
   price = models.IntegerField()
   status = models.CharField(max_length=50)