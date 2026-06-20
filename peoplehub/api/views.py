from django.shortcuts import render
from .models import Person
from .serializers import PersonModelSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.
@csrf_exempt
def singleobj(request,id):
    data = get_object_or_404(Person,id=id)
    if request.method == "PUT":
        json = request.body
        stream = io.BytesIO(json)
        parsed_data = JSONParser().parse(stream)
        serializer = PersonModelSerializer(data,data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"updated":"successfully"},status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PATCH":
        json = request.body
        stream = io.BytesIO(json)
        parsed_data = JSONParser().parse(stream)
        serializer = PersonModelSerializer(data,data=parsed_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"updated":"successfully"},status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    serializer = PersonModelSerializer(data)
    return JsonResponse(serializer.data)

@csrf_exempt
def multipleobj(request):
    if request.method == "POST":
        json = request.body
        stream = io.BytesIO(json)
        parsed_data = JSONParser().parse(stream)
        serializer = PersonModelSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"created":"successfully"},status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    data = Person.objects.all()
    serializer = PersonModelSerializer(data,many=True)
    return JsonResponse(serializer.data,safe=False)