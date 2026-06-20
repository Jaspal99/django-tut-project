from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Create your views here.
def singleobj(request):
    data = Person.objects.get(id=1)
    serializer = PersonSerializer(data)
    return JsonResponse(serializer.data)

@csrf_exempt
def multipleobj(request):
    if request.method == "POST":
        json = request.body
        stream = io.BytesIO(json)
        parsed_data = JSONParser().parse(stream)
        serializer = PersonSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"created":"successfully"},status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    data = Person.objects.all()
    serializer = PersonSerializer(data,many=True)
    return JsonResponse(serializer.data,safe=False)