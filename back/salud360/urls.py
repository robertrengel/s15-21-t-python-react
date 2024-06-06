from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi as oa
from rest_framework.documentation import include_docs_urls
from django.views.generic import RedirectView
from djoser.views import UserViewSet

# from rest_framework.documentation import include_docs_urls

# YOUR PATTERNS
admin.site.site_header = "Salud360 Admin Panel"


schema_view = get_schema_view(
    oa.Info(
        title="Doc360 Api",
        default_version="v1",
        description="This os the API documentation",
        lincense=oa.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.urls.authtoken")),
    path("users/", UserViewSet.as_view({"get": "list"})),
    path("api/", include("api.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("medical-history/", include("medical_history.api.v1.urls")),
    path("medic-profile/", include("medics_profile.api.v1.urls")),
    path("documents/", include("documents.urls")),
    path("catalogs/", include("catalogs.urls")),
    path("schema/", schema_view.as_view()),
    path(
        "docs/", include_docs_urls(title="Doc360 API services")
    ),  # Documentation endpoint
    path("", RedirectView.as_view(url="/docs/", permanent=True)),  # Re
]
