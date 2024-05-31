from django.urls import path
from . import views

urlpatterns = [
    path ('apiuser/', views.user_list),
    path ('apiuser/<int:id>', views.user_detail),
]
