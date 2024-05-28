from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ApiUser
from .serializers import UserSerializer

# def hola(request):
#    queryset = ApiUser.objects.all()
#    return render(request, 'test.html', {'users': queryset})


@api_view()
def user_list(request):
    queryset = ApiUser.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def user_detail(request, id):
    profile = get_object_or_404(ApiUser, pk=id)
    serializer = UserSerializer(profile)
    return Response(serializer.data)
