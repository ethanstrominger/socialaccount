from .models import Person
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PeopleSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows people to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('-name')
    serializer_class = PeopleSerializer
    permission_classes = [permissions.IsAuthenticated]

