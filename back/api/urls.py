from django.urls import path
from . import views

urlpatterns = [
    #path ('hello/', views.hola),
    path ('country/', views.countries_list),
    path ('country/<int:id>', views.country_detail),
    path ('role/', views.role_list),
    path ('role/<int:id>', views.role_detail),
]
