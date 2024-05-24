from django.urls import path
from . import views

urlpatterns = [
    #path ('hello/', views.hola),
    path ('apiuser/', views.user_list),
    path ('apiuser/<int:id>', views.user_detail),
    #path ('role/', views.role_list),
    #path ('role/<int:id>', views.role_detail),
]
