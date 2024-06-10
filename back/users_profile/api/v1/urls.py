from django.urls import path
from users_profile.api.v1.viewsets import (
    UserProfileViewSet,
    UserProfileUpdateViewSet,
)


user_profile_list = UserProfileViewSet.as_view(
    {
        "get": "list",
    }
)

user_profile_update = UserProfileUpdateViewSet.as_view(
    {
        "put": "update",
        "patch": "partial_update",
    }
)

urlpatterns = [
    path(
        "profile",
        user_profile_list,
        name="profile",
    ),
    path("profile/<int:pk>/", user_profile_update, name="user-profile-create"),
]
