from rest_framework import serializers

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=150)