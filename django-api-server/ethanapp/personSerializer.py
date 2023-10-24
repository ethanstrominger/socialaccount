from django.db import models

from .models import Person
from rest_framework import serializers


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['url', 'id', 'name']
