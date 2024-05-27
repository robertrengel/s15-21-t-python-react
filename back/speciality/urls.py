from django.urls import path
from . import views

urlpatterns = [
    path ('', views.speciality_list),
    path ('<int:id>', views.speciality_detail),
]
