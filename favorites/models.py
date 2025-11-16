from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class Favorite(models.Model):
    """User's favorite movies model."""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'movie')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'movie']),
        ]
    
    def __str__(self):
        return f"{self.user.username} favorited {self.movie.title}"
