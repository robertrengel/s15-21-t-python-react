from django.urls import path
from . import views
from .views import UserListView, CustomUserViewSet

urlpatterns = [
    path("apiuser/", UserListView.as_view()),
    path("apiuser/<int:id>", views.user_detail),
    path(
        "create-user/",
        CustomUserViewSet.as_view({"post": "create"}),
        name="create-user",
    ),
]
