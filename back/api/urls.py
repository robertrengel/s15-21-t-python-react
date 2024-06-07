from django.urls import path
from . import views
from .views import UserListView

urlpatterns = [
    path("apiuser/", UserListView.as_view()),
    path("apiuser/<int:id>", views.user_detail),
]
