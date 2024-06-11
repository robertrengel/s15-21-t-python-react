from django.urls import path
from .views import SpecialityViewSet, CountriesCatalogViewSet

speciality_list = SpecialityViewSet.as_view({"get": "list"})
country_list = CountriesCatalogViewSet.as_view({"get": "list"})

urlpatterns = [
    path("specialities/", speciality_list, name="speciality-list"),
    path("countries/", country_list, name="country-list"),
]
