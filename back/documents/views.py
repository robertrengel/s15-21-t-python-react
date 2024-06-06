from rest_framework import viewsets
from .models import Documents
from .serializers import DocumentsSerializer

class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer