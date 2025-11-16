from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie
from .serializers import MovieSerializer, MovieDetailSerializer


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Movie model with filtering, searching, and pagination.
    Endpoints:
    - GET /movies/ - List all movies with filters and search
    - GET /movies/<id>/ - Retrieve single movie
    """
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'year', 'category']
    search_fields = ['title', 'description']
    ordering_fields = ['year', 'created_at', 'title']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Use detailed serializer for retrieve action."""
        if self.action == 'retrieve':
            return MovieDetailSerializer
        return MovieSerializer
    
    def list(self, request, *args, **kwargs):
        """
        List movies with optional filters and search.
        Query parameters:
        - search: Search in title and description (max 100 chars)
        - genre: Filter by genre
        - year: Filter by year
        - category: Filter by category
        - page: Page number (default 1)
        """
        # Validate search parameter size to prevent ReDoS
        search_param = request.query_params.get('search', '')
        if len(search_param) > 100:
            return Response(
                {'error': 'Search parameter must be less than 100 characters.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return super().list(request, *args, **kwargs)
