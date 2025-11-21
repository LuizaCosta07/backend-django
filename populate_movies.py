import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gatoflix.settings')
django.setup()

from movies.models import Movie
from django.core.management.base import BaseCommand

movies_data = [
    {
        "title": "O Poderoso Gatão",
        "description": "O patriarca de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante. Uma obra-prima do cinema felino.",
        "year": 1972,
        "genre": "Feline-thriller",
        "category": "movie",
        "poster_url": "https://image.tmdb.org/t/p/w500/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
        "banner_url": "https://image.tmdb.org/t/p/original/tmU7GeKVybMWFButWEGl2M4GeiP.jpg",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "duration": "2h 55m",
        "rating": 9.8,
        "cast": "Marlon Brando, Al Pacino, James Caan"
    },
    {
        "title": "Gatos e Furiosos",
        "description": "Um policial se infiltra no mundo das corridas de rua de Los Angeles para capturar uma gangue de sequestradores. Muita velocidade e sachê.",
        "year": 2001,
        "genre": "Tiger-action",
        "category": "movie",
        "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "banner_url": "https://image.tmdb.org/t/p/original/n2y7T8wJVjJ8yLhPLbLuMLwmhI.jpg",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "duration": "1h 46m",
        "rating": 7.8,
        "cast": "Vin Diesel, Paul Walker, Michelle Rodriguez"
    },
    {
        "title": "Miau Missão Impossível",
        "description": "Um agente americano, sob falsa suspeita de deslealdade, deve descobrir e expor o verdadeiro espião sem a ajuda de sua organização.",
        "year": 1996,
        "genre": "Tiger-action",
        "category": "movie",
        "poster_url": "https://image.tmdb.org/t/p/w500/AkJQpZp9WoNdj7pLYSj1L0RcMMN.jpg",
        "banner_url": "https://image.tmdb.org/t/p/original/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "duration": "1h 50m",
        "rating": 8.5,
        "cast": "Tom Cruise, Jon Voight, Emmanuelle Béart"
    },
    {
        "title": "Gatman: O Cavaleiro das Trevas",
        "description": "Quando a ameaça conhecida como Coringa causa estragos e caos no povo de Gotham, Batman deve aceitar um dos maiores testes psicológicos e físicos de sua capacidade de lutar contra a injustiça.",
        "year": 2008,
        "genre": "Tiger-action",
        "category": "movie",
        "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "banner_url": "https://image.tmdb.org/t/p/original/hkBaDkMWbLaf8B1lsWsKX7Ew3Xq.jpg",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "duration": "2h 32m",
        "rating": 9.9,
        "cast": "Christian Bale, Heath Ledger, Aaron Eckhart"
    },
    {
        "title": "Interestelar: A Jornada Felina",
        "description": "Uma equipe de exploradores viaja através de um buraco de minhoca no espaço na tentativa de garantir a sobrevivência da humanidade.",
        "year": 2014,
        "genre": "Whisker-sci-fi",
        "category": "movie",
        "poster_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
        "banner_url": "https://image.tmdb.org/t/p/original/rAiYTfKGqDCRIIqo664sY9XZIvQ.jpg",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "duration": "2h 49m",
        "rating": 9.5,
        "cast": "Matthew McConaughey, Anne Hathaway, Jessica Chastain"
    },
     {
        "title": "La Casa de Papelão",
        "description": "Um grupo de gatos planeja o maior roubo da história: entrar na fábrica de caixas de papelão.",
        "year": 2017,
        "genre": "Feline-thriller",
        "category": "series",
        "poster_url": "https://image.tmdb.org/t/p/w500/reEMJA1uzscCbkpeRJeTT2bjqUp.jpg",
        "banner_url": "https://image.tmdb.org/t/p/original/xGexTKCJDkl12dTW4YCBDXWb1AD.jpg",
        "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "duration": "5 Temporadas",
        "rating": 8.8,
        "cast": "Úrsula Corberó, Álvaro Morte, Itziar Ituño"
    }
]

# Clear existing movies to avoid duplicates/conflicts with old data structure
Movie.objects.all().delete()
print("Cleared existing movies.")

for movie_data in movies_data:
    Movie.objects.create(**movie_data)
    print(f"Created: {movie_data['title']}")
