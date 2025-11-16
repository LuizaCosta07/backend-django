from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Serializer for Movie model."""
    
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'description',
            'year',
            'genre',
            'category',
            'poster_url',
            'video_url',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']


class MovieDetailSerializer(MovieSerializer):
    """Extended serializer for detailed movie view."""
    
    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ['updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
