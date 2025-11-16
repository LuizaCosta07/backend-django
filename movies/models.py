from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from django.utils.timezone import now


class Movie(models.Model):
    """Cat-themed movie model for GatoFlix."""
    
    GENRE_CHOICES = [
        ('Feline-thriller', 'Feline-thriller'),
        ('Cat-edy', 'Cat-edy'),
        ('Purr-drama', 'Purr-drama'),
        ('Whisker-sci-fi', 'Whisker-sci-fi'),
        ('Paw-western', 'Paw-western'),
        ('Meow-horror', 'Meow-horror'),
        ('Kitten-romance', 'Kitten-romance'),
        ('Tiger-action', 'Tiger-action'),
    ]
    
    CATEGORY_CHOICES = [
        ('movie', 'Movie'),
        ('series', 'Series'),
        ('documentary', 'Documentary'),
    ]
    
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    year = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2100)]
    )
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='movie')
    poster_url = models.URLField(
        validators=[URLValidator()],
        help_text="Valid HTTPS or HTTP URL to poster image"
    )
    video_url = models.URLField(
        validators=[URLValidator()],
        help_text="Valid HTTPS or HTTP URL to video"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['genre']),
            models.Index(fields=['year']),
            models.Index(fields=['title']),
        ]
    
    def __str__(self):
        return f"{self.title} ({self.year})"
