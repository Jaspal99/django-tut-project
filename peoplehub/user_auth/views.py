from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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