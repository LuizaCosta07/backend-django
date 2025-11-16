"""
Comprehensive unit tests for GatoFlix API.
Run with: python manage.py test
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from movies.models import Movie
from favorites.models import Favorite


class MovieModelTests(TestCase):
    """Tests for Movie model."""

    def setUp(self):
        """Set up test data."""
        self.movie = Movie.objects.create(
            title="O Gato das Sombras",
            description="Um gato misterioso viaja através do tempo",
            year=2023,
            genre="Feline-thriller",
            category="movie",
            poster_url="https://placekitten.com/300/450?image=1",
            video_url="https://example.com/video1",
        )

    def test_movie_creation(self):
        """Test movie is created correctly."""
        self.assertEqual(self.movie.title, "O Gato das Sombras")
        self.assertEqual(self.movie.year, 2023)
        self.assertEqual(self.movie.genre, "Feline-thriller")

    def test_movie_string_representation(self):
        """Test movie __str__ method."""
        expected = "O Gato das Sombras (2023)"
        self.assertEqual(str(self.movie), expected)

    def test_movie_valid_genres(self):
        """Test all valid genre choices."""
        valid_genres = [
            "Feline-thriller",
            "Cat-edy",
            "Purr-drama",
            "Whisker-sci-fi",
            "Paw-western",
            "Meow-horror",
            "Kitten-romance",
            "Tiger-action",
        ]
        for genre in valid_genres:
            movie = Movie.objects.create(
                title=f"Movie {genre}",
                description="Test",
                year=2023,
                genre=genre,
                category="movie",
                poster_url="https://example.com/poster.jpg",
                video_url="https://example.com/video.mp4",
            )
            self.assertEqual(movie.genre, genre)

    def test_movie_valid_categories(self):
        """Test all valid category choices."""
        valid_categories = ["movie", "series", "documentary"]
        for category in valid_categories:
            movie = Movie.objects.create(
                title=f"Movie {category}",
                description="Test",
                year=2023,
                genre="Feline-thriller",
                category=category,
                poster_url="https://example.com/poster.jpg",
                video_url="https://example.com/video.mp4",
            )
            self.assertEqual(movie.category, category)

    def test_movie_year_validation(self):
        """Test year validators."""
        # Valid year
        movie = Movie.objects.create(
            title="Valid Year",
            description="Test",
            year=1950,
            genre="Feline-thriller",
            category="movie",
            poster_url="https://example.com/poster.jpg",
            video_url="https://example.com/video.mp4",
        )
        self.assertEqual(movie.year, 1950)

    def test_movie_ordering(self):
        """Test movies are ordered by created_at descending."""
        import time
        movie2 = Movie.objects.create(
            title="Newer Movie",
            description="Test",
            year=2024,
            genre="Cat-edy",
            category="movie",
            poster_url="https://example.com/poster.jpg",
            video_url="https://example.com/video.mp4",
        )
        time.sleep(0.01)
        movie3 = Movie.objects.create(
            title="Newest Movie",
            description="Test",
            year=2025,
            genre="Tiger-action",
            category="movie",
            poster_url="https://example.com/poster.jpg",
            video_url="https://example.com/video.mp4",
        )
        movies = Movie.objects.filter(title__in=["Newer Movie", "Newest Movie"]).order_by("-created_at")
        self.assertEqual(movies[0], movie3)
        self.assertEqual(movies[1], movie2)


class FavoriteModelTests(TestCase):
    """Tests for Favorite model."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test",
            year=2023,
            genre="Feline-thriller",
            category="movie",
            poster_url="https://example.com/poster.jpg",
            video_url="https://example.com/video.mp4",
        )

    def test_favorite_creation(self):
        """Test favorite is created correctly."""
        favorite = Favorite.objects.create(user=self.user, movie=self.movie)
        self.assertEqual(favorite.user, self.user)
        self.assertEqual(favorite.movie, self.movie)

    def test_favorite_string_representation(self):
        """Test favorite __str__ method."""
        favorite = Favorite.objects.create(user=self.user, movie=self.movie)
        expected = f"testuser favorited Test Movie"
        self.assertEqual(str(favorite), expected)

    def test_favorite_unique_constraint(self):
        """Test unique_together constraint on (user, movie)."""
        Favorite.objects.create(user=self.user, movie=self.movie)
        with self.assertRaises(Exception):
            Favorite.objects.create(user=self.user, movie=self.movie)

    def test_favorite_ordering(self):
        """Test favorites are ordered by created_at descending."""
        import time
        fav1 = Favorite.objects.create(user=self.user, movie=self.movie)
        time.sleep(0.01)
        movie2 = Movie.objects.create(
            title="Another Movie",
            description="Test",
            year=2023,
            genre="Cat-edy",
            category="movie",
            poster_url="https://example.com/poster.jpg",
            video_url="https://example.com/video.mp4",
        )
        fav2 = Favorite.objects.create(user=self.user, movie=movie2)
        favorites = Favorite.objects.filter(user=self.user)
        self.assertEqual(favorites[0], fav2)
        self.assertEqual(favorites[1], fav1)


class MovieAPITests(APITestCase):
    """Tests for Movie API endpoints."""

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.movie_url = "/movies/"
        
        # Create test movies
        self.movie1 = Movie.objects.create(
            title="O Gato das Sombras",
            description="Um gato misterioso viaja através do tempo",
            year=2023,
            genre="Feline-thriller",
            category="movie",
            poster_url="https://placekitten.com/300/450?image=1",
            video_url="https://example.com/video1",
        )
        
        self.movie2 = Movie.objects.create(
            title="Gatadas: O Retorno",
            description="Uma comédia hilariante sobre um gato",
            year=2022,
            genre="Cat-edy",
            category="movie",
            poster_url="https://placekitten.com/300/450?image=2",
            video_url="https://example.com/video2",
        )

    def test_list_movies(self):
        """Test listing all movies."""
        response = self.client.get(self.movie_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(len(response.data["results"]), 2)

    def test_list_movies_pagination(self):
        """Test movie list is paginated."""
        response = self.client.get(self.movie_url)
        self.assertIn("count", response.data)
        self.assertIn("next", response.data)
        self.assertIn("previous", response.data)
        self.assertIn("results", response.data)

    def test_get_movie_detail(self):
        """Test getting single movie detail."""
        response = self.client.get(f"{self.movie_url}{self.movie1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "O Gato das Sombras")
        self.assertEqual(response.data["year"], 2023)

    def test_get_nonexistent_movie(self):
        """Test getting non-existent movie returns 404."""
        response = self.client.get(f"{self.movie_url}999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_movies_by_genre(self):
        """Test filtering movies by genre."""
        response = self.client.get(f"{self.movie_url}?genre=Feline-thriller")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], "O Gato das Sombras")

    def test_filter_movies_by_year(self):
        """Test filtering movies by year."""
        response = self.client.get(f"{self.movie_url}?year=2022")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], "Gatadas: O Retorno")

    def test_filter_movies_by_category(self):
        """Test filtering movies by category."""
        # Create a series
        Movie.objects.create(
            title="Test Series",
            description="Test",
            year=2023,
            genre="Cat-edy",
            category="series",
            poster_url="https://example.com/poster.jpg",
            video_url="https://example.com/video.mp4",
        )
        
        response = self.client.get(f"{self.movie_url}?category=series")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_search_movies_by_title(self):
        """Test searching movies by title."""
        response = self.client.get(f"{self.movie_url}?search=Sombras")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], "O Gato das Sombras")

    def test_search_movies_by_description(self):
        """Test searching movies by description."""
        response = self.client.get(f"{self.movie_url}?search=misterioso")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_search_case_insensitive(self):
        """Test search is case insensitive."""
        response = self.client.get(f"{self.movie_url}?search=GATO")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data["count"], 1)

    def test_movie_cannot_be_created_via_api(self):
        """Test movies cannot be created via API (read-only)."""
        data = {
            "title": "New Movie",
            "description": "Test",
            "year": 2024,
            "genre": "Feline-thriller",
            "category": "movie",
            "poster_url": "https://example.com/poster.jpg",
            "video_url": "https://example.com/video.mp4",
        }
        response = self.client.post(self.movie_url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_movie_detail_includes_updated_at(self):
        """Test movie detail includes updated_at field."""
        response = self.client.get(f"{self.movie_url}{self.movie1.id}/")
        self.assertIn("updated_at", response.data)


class UserRegistrationTests(APITestCase):
    """Tests for user registration endpoint."""

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.register_url = "/auth/register/"

    def test_user_registration_success(self):
        """Test successful user registration."""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "SenhaForte123",
            "password_confirm": "SenhaForte123",
            "first_name": "Test",
            "last_name": "User",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)
        self.assertEqual(response.data["user"]["username"], "newuser")

    def test_registration_password_mismatch(self):
        """Test registration fails with mismatched passwords."""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "securepass123",
            "password_confirm": "differentpass123",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_duplicate_username(self):
        """Test registration fails with duplicate username."""
        User.objects.create_user(
            username="existinguser",
            email="existing@example.com",
            password="pass123",
        )
        data = {
            "username": "existinguser",
            "email": "newemail@example.com",
            "password": "pass123",
            "password_confirm": "pass123",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_duplicate_email(self):
        """Test registration fails with duplicate email."""
        User.objects.create_user(
            username="user1",
            email="existing@example.com",
            password="pass123",
        )
        data = {
            "username": "newuser",
            "email": "existing@example.com",
            "password": "pass123",
            "password_confirm": "pass123",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_returns_tokens(self):
        """Test registration returns JWT tokens."""
        data = {
            "username": "newuser2",
            "email": "newuser2@example.com",
            "password": "SenhaForte123",
            "password_confirm": "SenhaForte123",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        tokens = response.data
        self.assertIsNotNone(tokens["access"])
        self.assertIsNotNone(tokens["refresh"])
        # Tokens should be strings
        self.assertIsInstance(tokens["access"], str)
        self.assertIsInstance(tokens["refresh"], str)


class UserLoginTests(APITestCase):
    """Tests for user login endpoint."""

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.login_url = "/auth/login/"
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )

    def test_user_login_success(self):
        """Test successful user login."""
        data = {"username": "testuser", "password": "testpass123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)

    def test_login_invalid_credentials(self):
        """Test login fails with invalid credentials."""
        data = {"username": "testuser", "password": "wrongpassword"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_nonexistent_user(self):
        """Test login fails with non-existent user."""
        data = {"username": "nonexistent", "password": "password"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_returns_tokens(self):
        """Test login returns JWT tokens."""
        data = {"username": "testuser", "password": "testpass123"}
        response = self.client.post(self.login_url, data)
        
        tokens = response.data
        self.assertIsNotNone(tokens["access"])
        self.assertIsNotNone(tokens["refresh"])


class UserDetailTests(APITestCase):
    """Tests for user detail endpoint."""

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.me_url = "/auth/me/"
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            first_name="Test",
            last_name="User",
        )

    def test_get_current_user_authenticated(self):
        """Test getting current user when authenticated."""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.me_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")
        self.assertEqual(response.data["email"], "test@example.com")

    def test_get_current_user_unauthenticated(self):
        """Test getting current user without authentication."""
        response = self.client.get(self.me_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class FavoriteAPITests(APITestCase):
    """Tests for Favorite API endpoints."""

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.favorites_url = "/favorites/"
        
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test",
            year=2023,
            genre="Feline-thriller",
            category="movie",
            poster_url="https://example.com/poster.jpg",
            video_url="https://example.com/video.mp4",
        )
        
        self.client.force_authenticate(user=self.user)

    def test_add_favorite_success(self):
        """Test successfully adding movie to favorites."""
        response = self.client.post(f"{self.favorites_url}{self.movie.id}/add/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["movie"]["id"], self.movie.id)

    def test_add_duplicate_favorite(self):
        """Test adding duplicate favorite returns error."""
        self.client.post(f"{self.favorites_url}{self.movie.id}/add/")
        response = self.client.post(f"{self.favorites_url}{self.movie.id}/add/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_remove_favorite_success(self):
        """Test successfully removing movie from favorites."""
        Favorite.objects.create(user=self.user, movie=self.movie)
        response = self.client.delete(f"{self.favorites_url}{self.movie.id}/remove/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Favorite.objects.filter(user=self.user, movie=self.movie).exists()
        )

    def test_remove_nonexistent_favorite(self):
        """Test removing non-existent favorite returns 404."""
        response = self.client.delete(f"{self.favorites_url}{self.movie.id}/remove/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_favorites(self):
        """Test listing user's favorites."""
        Favorite.objects.create(user=self.user, movie=self.movie)
        response = self.client.get(self.favorites_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_list_favorites_empty(self):
        """Test listing favorites when none exist."""
        response = self.client.get(self.favorites_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)

    def test_favorites_requires_authentication(self):
        """Test favorites endpoints require authentication."""
        self.client.force_authenticate(user=None)
        response = self.client.get(self.favorites_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_only_sees_own_favorites(self):
        """Test user only sees their own favorites."""
        Favorite.objects.create(user=self.user, movie=self.movie)
        
        other_user = User.objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="pass123",
        )
        self.client.force_authenticate(user=other_user)
        
        response = self.client.get(self.favorites_url)
        self.assertEqual(response.data["count"], 0)


class FavoriteWithMultipleMoviesTests(APITestCase):
    """Tests for favorites with multiple movies."""

    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.favorites_url = "/favorites/"
        
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        
        self.movies = []
        for i in range(15):
            movie = Movie.objects.create(
                title=f"Movie {i}",
                description=f"Description {i}",
                year=2023,
                genre="Feline-thriller",
                category="movie",
                poster_url=f"https://example.com/poster{i}.jpg",
                video_url=f"https://example.com/video{i}.mp4",
            )
            self.movies.append(movie)
        
        self.client.force_authenticate(user=self.user)

    def test_favorites_pagination(self):
        """Test favorites are paginated with 10 items per page."""
        # Add 15 movies to favorites
        for movie in self.movies:
            Favorite.objects.create(user=self.user, movie=movie)
        
        # Get first page
        response = self.client.get(f"{self.favorites_url}?page=1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 10)
        self.assertIsNotNone(response.data["next"])
        
        # Get second page
        response = self.client.get(f"{self.favorites_url}?page=2")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 5)
        self.assertIsNone(response.data["next"])
