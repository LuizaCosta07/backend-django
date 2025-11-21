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
    banner_url = models.URLField(
        validators=[URLValidator()],
        help_text="Wide banner image for hero section",
        blank=True, null=True
    )
    video_url = models.URLField(
        validators=[URLValidator()],
        help_text="Valid HTTPS or HTTP URL to video"
    )
    duration = models.CharField(max_length=20, help_text="e.g., '1h 45m' or '2 Seasons'", default="Unknown")
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0,
        help_text="Rating from 0.0 to 10.0"
    )
    cast = models.TextField(help_text="Comma-separated list of actors", blank=True)
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
