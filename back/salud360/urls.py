"""
URL configuration for salud360 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# <<<<<<< HEAD
# from rest_framework.documentation import include_docs_urls

# admin.site.site_header = "Salud360 Admin Panel"

# urlpatterns = [
#    path("admin/", admin.site.urls),
#    path("api/", include("api.urls")),
#    path("__debug__/", include("debug_toolbar.urls")),
# =======

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# from rest_framework.authtoken import views

from rest_framework.documentation import include_docs_urls

# YOUR PATTERNS
admin.site.site_header = "Salud360 Admin Panel"

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Doc360",
#         default_version="v1.0",
#         description="Documentacion",
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )


urlpatterns = [
    # path(
    #     "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    # ),
    # path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    # path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path(
        "api/v1/medical-history/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui-medical_history",
    ),
    path(
        "api/v1/medics-profile/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui-medics_profile",
    ),
    path("api/v1/medical-history/", include("medical_history.api.v1.urls")),
    path("api/v1/medics-profile/", include("medics_profile.api.v1.urls")),
    # >>>>>>> f005-resc/medical-history-documentation
    path("docs/", include_docs_urls(title="API Documentation")),
]
