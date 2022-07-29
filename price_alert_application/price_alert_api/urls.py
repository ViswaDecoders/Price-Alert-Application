from django.urls import path
from .views import Alert_Api

urlpatterns = [
    path('alerts/create', Alert_Api.as_view()),
    path('alerts', Alert_Api.as_view()),
]
