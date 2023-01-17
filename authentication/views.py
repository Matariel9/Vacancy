from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .serializers import UserCreateSerializer
from .models import User

# Create your views here.

class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer

class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)