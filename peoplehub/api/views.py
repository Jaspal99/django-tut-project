from django.shortcuts import render
from .models import Person
from .serializers import PersonModelSerializer
from rest_framework.renderers import JSONRenderer
# from django.http import Response
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin

# Create your views here.
@api_view(["GET","PATCH","PUT"])
def singleobj(request,id):
    data = get_object_or_404(Person,id=id)
    if request.method == "PUT":
        serializer = PersonModelSerializer(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"updated":"successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PATCH":
        serializer = PersonModelSerializer(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"updated":"successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    serializer = PersonModelSerializer(data)
    return Response(serializer.data)

@api_view(["GET","PATCH","PUT"])
def multipleobj(request):
    if request.method == "POST":
        serializer = PersonModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"created":"successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    data = Person.objects.all()
    serializer = PersonModelSerializer(data,many=True)
    return Response(serializer.data)


class SingleObjAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer

class MultiObjAPIView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer