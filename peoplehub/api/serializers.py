from rest_framework import serializers
from .models import Person
class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=150)

    def create(self,validated_data):
        return Person.objects.create(**validated_data)