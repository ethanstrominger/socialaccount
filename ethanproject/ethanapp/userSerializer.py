from django.db import models

from django.contrib.auth.models import User
from rest_framework import serializers

print("serializer")
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email']

