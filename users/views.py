from django.shortcuts import render

# Create your views here.


# Registration View
from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]