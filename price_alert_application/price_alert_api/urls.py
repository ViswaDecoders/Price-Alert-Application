from django.urls import path
from .views import AlertAdd

urlpatterns = [
    path('alerts/create', AlertAdd.as_view()),
]
