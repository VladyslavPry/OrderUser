from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['POST'])
def LoginView(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        return Response({"message":"Login done"}, status=status.HTTP_200_OK)
    return Response({"message": "Invalid smt"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def LogoutView(request):
    logout(request)
    return Response({"message": "Logged out"}, status=status.HTTP_200_OK)
