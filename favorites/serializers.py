from rest_framework import serializers
from movies.serializers import MovieSerializer
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    """Serializer for Favorite model."""
    
    movie = MovieSerializer(read_only=True)
    
    class Meta:
        model = Favorite
        fields = ['id', 'movie', 'created_at']
        read_only_fields = ['id', 'created_at']
