from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentsViewSet

router = DefaultRouter()
router.register(r'documents', DocumentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]