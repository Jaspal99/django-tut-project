from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username","password"]

    def create(self, validated_data):
        # NOTE: validated_data = {'username': 'bob', 'password': 'pw'}
        # # correct
        # User.objects.create_user(**validated_data)   # -> create_user(username='bob', password='pw')
        # # incorrect
        # User.objects.create_user(validated_data)    # -> username receives the dict -> error/invalid
        return User.objects.create_user(**validated_data)