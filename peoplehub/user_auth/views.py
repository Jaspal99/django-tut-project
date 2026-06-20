from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterSerializer

class LoginAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username,password=password)
        if user is None:
            return Response({"error":"Invalid credentials"},status=status.HTTP_401_UNAUTHORIZED)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key})
    
class UserRegistration(APIView):
    permission_classes = []
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"User created successfully"},status=status.HTTP_201_CREATED)
    
class LogoutAPIView(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response("logout successfull")