
from rest_framework import generics, permissions
from django.contrib.auth.models import User

# Create your views here.
from api.permissions import IsOwnerOrSuperReadOnly
from movie.models import Movie
from movie.serializers import MovieSerializer


class ListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrSuperReadOnly)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        user = User.objects.get(pk=1)
        serializer.save(owner=user)

class DetailAndUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrSuperReadOnly)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer