from django.urls import path
from .views import Alert_Api,User_Create,User_Login,User_Logout

urlpatterns = [
    path('users/create', User_Create.as_view()),
    path('users/Login', User_Login.as_view()),
    path('users/Logout', User_Logout.as_view()),
    path('alerts/create', Alert_Api.as_view()),
    path('alerts', Alert_Api.as_view()),
    path('alerts/delete<int:item_id>', Alert_Api.as_view()),
]
