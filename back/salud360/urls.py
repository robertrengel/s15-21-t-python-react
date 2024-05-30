from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi as oa
from rest_framework.documentation import include_docs_urls
from django.views.generic import RedirectView

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
    path("api/", include("api.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("medical-history/", include("medical_history.api.v1.urls")),
    path("medic-profile/", include("medics_profile.api.v1.urls")),
    path("catalogs/", include("catalogs.urls")),
    path("schema/", schema_view.as_view()),
    path(
        "docs/", include_docs_urls(title="Doc360 API services")
    ),  # Documentation endpoint
    path("", RedirectView.as_view(url="/docs/", permanent=True)),  # Re
]
