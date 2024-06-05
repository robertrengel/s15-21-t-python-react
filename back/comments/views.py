from rest_framework import viewsets
from .serializer import CommentSerializer
from .models import Comment
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
