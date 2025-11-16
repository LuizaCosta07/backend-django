from rest_framework import status, views, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from movies.models import Movie
from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    ViewSet for user favorite movies management.
    Endpoints:
    - GET /favorites/ - List user's favorite movies
    - POST /favorites/<movie_id>/add/ - Add movie to favorites
    - DELETE /favorites/<movie_id>/remove/ - Remove movie from favorites
    """
    
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']
    
    def get_queryset(self):
        """Return only current user's favorites."""
        return Favorite.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['post'], url_path='(?P<movie_id>[^/.]+)/add')
    def add_favorite(self, request, movie_id=None):
        """
        Add movie to user's favorites.
        POST /favorites/<movie_id>/add/
        Returns: 201 Created
        """
        movie = get_object_or_404(Movie, id=movie_id)
        
        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            movie=movie
        )
        
        if not created:
            return Response(
                {'detail': 'Este filme já está nos favoritos.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['delete'], url_path='(?P<movie_id>[^/.]+)/remove')
    def remove_favorite(self, request, movie_id=None):
        """
        Remove movie from user's favorites.
        DELETE /favorites/<movie_id>/remove/
        Returns: 204 No Content
        """
        favorite = get_object_or_404(
            Favorite,
            user=request.user,
            movie_id=movie_id
        )
        favorite.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        """
        List user's favorite movies with pagination.
        GET /favorites/
        Returns: Paginated list of favorites
        """
        return super().list(request, *args, **kwargs)
