from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def singleobj(request):
    data = Person.objects.get(id=1)
    serializer = PersonSerializer(data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


def multipleobj(request):
    data = Person.objects.all()
    serializer = PersonSerializer(data,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')