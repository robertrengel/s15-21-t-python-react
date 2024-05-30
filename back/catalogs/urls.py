from django.urls import path
from .views import SpecialityViewSet

speciality_list = SpecialityViewSet.as_view({"get": "list"})
speciality_detail = SpecialityViewSet.as_view({"get": "retrieve"})
urlpatterns = [
    path("specialities/", speciality_list, name="speciality-list"),
]
