from .models import Movie
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-title')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

