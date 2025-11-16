from django.core.management.base import BaseCommand
from movies.models import Movie


class Command(BaseCommand):
    """Management command to seed the database with cat-themed movies."""
    
    help = 'Seed the database with 30 cat-themed movies'
    
    CAT_MOVIES = [
        {
            'title': 'O Gato das Sombras',
            'description': 'Um gato misterioso viaja através do tempo para salvar a humanidade de uma ameaça sombria.',
            'year': 2023,
            'genre': 'Feline-thriller',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=1',
            'video_url': 'https://example.com/video1',
        },
        {
            'title': 'Gatadas: O Retorno',
            'description': 'Uma comédia hilariante sobre um gato que se torna ator de Hollywood.',
            'year': 2022,
            'genre': 'Cat-edy',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=2',
            'video_url': 'https://example.com/video2',
        },
        {
            'title': 'Ronrom: Uma História de Amor',
            'description': 'Dois gatos se conhecem em um abrigo e vivem um romance inesperado.',
            'year': 2021,
            'genre': 'Kitten-romance',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=3',
            'video_url': 'https://example.com/video3',
        },
        {
            'title': 'O Último Minino',
            'description': 'Um gato pós-apocalíptico tenta sobreviver em um mundo devastado.',
            'year': 2024,
            'genre': 'Purr-drama',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=4',
            'video_url': 'https://example.com/video4',
        },
        {
            'title': 'Intergalático Felino',
            'description': 'Um gato astronauta explora galáxias desconhecidas em busca da Lenda Perdida.',
            'year': 2025,
            'genre': 'Whisker-sci-fi',
            'category': 'series',
            'poster_url': 'https://placekitten.com/300/450?image=5',
            'video_url': 'https://example.com/video5',
        },
        {
            'title': 'O Xerife Bigodudo',
            'description': 'Um gato velho e astuto é o único que pode trazer justiça ao Velho Oeste.',
            'year': 2020,
            'genre': 'Paw-western',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=6',
            'video_url': 'https://example.com/video6',
        },
        {
            'title': 'Pesadelo Felino',
            'description': 'Um gato enfrenta seus medos mais profundos em uma mansão assombrada.',
            'year': 2023,
            'genre': 'Meow-horror',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=7',
            'video_url': 'https://example.com/video7',
        },
        {
            'title': 'Arranhador: Guerreiro Felino',
            'description': 'Um gato ninja treina para derrotar o Senhor da Escuridão Felina.',
            'year': 2024,
            'genre': 'Tiger-action',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=8',
            'video_url': 'https://example.com/video8',
        },
        {
            'title': 'Gatato: O Príncipe Perdido',
            'description': 'Um filhote é o herdeiro perdido de um reino felino ancestral.',
            'year': 2022,
            'genre': 'Purr-drama',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=9',
            'video_url': 'https://example.com/video9',
        },
        {
            'title': 'Miau Impossível',
            'description': 'Um gato espião executa missões secretas pelo mundo.',
            'year': 2023,
            'genre': 'Tiger-action',
            'category': 'series',
            'poster_url': 'https://placekitten.com/300/450?image=10',
            'video_url': 'https://example.com/video10',
        },
        {
            'title': 'Rindo com Felinos',
            'description': 'Uma série de episódios engraçados sobre a vida cotidiana de gatos.',
            'year': 2023,
            'genre': 'Cat-edy',
            'category': 'series',
            'poster_url': 'https://placekitten.com/300/450?image=11',
            'video_url': 'https://example.com/video11',
        },
        {
            'title': 'A Revolta do Sofá',
            'description': 'Gatos domésticos se unem para conquistar sua liberdade.',
            'year': 2024,
            'genre': 'Tiger-action',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=12',
            'video_url': 'https://example.com/video12',
        },
        {
            'title': 'Viagem para o Coração Felino',
            'description': 'Dois gatos amigos viajam pelo mundo em busca de significado.',
            'year': 2021,
            'genre': 'Purr-drama',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=13',
            'video_url': 'https://example.com/video13',
        },
        {
            'title': 'Segredos da Noite Felina',
            'description': 'Um documentário sobre os mistérios nocturnos dos gatos selvagens.',
            'year': 2023,
            'genre': 'Feline-thriller',
            'category': 'documentary',
            'poster_url': 'https://placekitten.com/300/450?image=14',
            'video_url': 'https://example.com/video14',
        },
        {
            'title': 'O Grande Roubo do Atum',
            'description': 'Três gatos planejam o roubo mais audacioso da história felina.',
            'year': 2022,
            'genre': 'Cat-edy',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=15',
            'video_url': 'https://example.com/video15',
        },
        {
            'title': 'Galáxia Minina',
            'description': 'Uma aventura intergaláctica com gatos e alienígenas felinos.',
            'year': 2025,
            'genre': 'Whisker-sci-fi',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=16',
            'video_url': 'https://example.com/video16',
        },
        {
            'title': 'O Código do Gato',
            'description': 'Um hacker felino rouba arquivos secretos do governo.',
            'year': 2023,
            'genre': 'Feline-thriller',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=17',
            'video_url': 'https://example.com/video17',
        },
        {
            'title': 'Corações Felinos Encontram',
            'description': 'Um gato urbano se apaixona por um gato selvagem na floresta.',
            'year': 2024,
            'genre': 'Kitten-romance',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=18',
            'video_url': 'https://example.com/video18',
        },
        {
            'title': 'Meow Grito',
            'description': 'Um terror silencioso afeta a população felina de uma pequena cidade.',
            'year': 2022,
            'genre': 'Meow-horror',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=19',
            'video_url': 'https://example.com/video19',
        },
        {
            'title': 'Os Sete Gatos Magníficos',
            'description': 'Sete gatos bandidos se reúnem para uma última grande missão.',
            'year': 2021,
            'genre': 'Paw-western',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=20',
            'video_url': 'https://example.com/video20',
        },
        {
            'title': 'Resgate Felino',
            'description': 'Um gato bombeiro salva vidas em operações de resgate dramáticas.',
            'year': 2023,
            'genre': 'Purr-drama',
            'category': 'series',
            'poster_url': 'https://placekitten.com/300/450?image=21',
            'video_url': 'https://example.com/video21',
        },
        {
            'title': 'A Sombra do Tigre',
            'description': 'Um gato selvagem procura vingança contra os humanos que destruíram sua floresta.',
            'year': 2024,
            'genre': 'Feline-thriller',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=22',
            'video_url': 'https://example.com/video22',
        },
        {
            'title': 'Gatuto: A Lenda Continua',
            'description': 'Um gato jovem segue os passos de seu herói lendário.',
            'year': 2025,
            'genre': 'Tiger-action',
            'category': 'series',
            'poster_url': 'https://placekitten.com/300/450?image=23',
            'video_url': 'https://example.com/video23',
        },
        {
            'title': 'Amor em Tempos de Pura Felicidade',
            'description': 'Um romance clássico ambientado em uma colônia felina.',
            'year': 2022,
            'genre': 'Kitten-romance',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=24',
            'video_url': 'https://example.com/video24',
        },
        {
            'title': 'Futurista Felino 2050',
            'description': 'Gatos robôs enfrentam uma inteligência artificial maligna.',
            'year': 2025,
            'genre': 'Whisker-sci-fi',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=25',
            'video_url': 'https://example.com/video25',
        },
        {
            'title': 'Gatilho da Justiça',
            'description': 'Um policial felino trabalha para resolver crimes em uma metrópole.',
            'year': 2024,
            'genre': 'Feline-thriller',
            'category': 'series',
            'poster_url': 'https://placekitten.com/300/450?image=26',
            'video_url': 'https://example.com/video26',
        },
        {
            'title': 'Gato Forte Explode',
            'description': 'Um super-herói felino protege a cidade da destruição.',
            'year': 2023,
            'genre': 'Tiger-action',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=27',
            'video_url': 'https://example.com/video27',
        },
        {
            'title': 'A Profecia do Sétimo Miau',
            'description': 'Um gato antigo profetiza o futuro da civilização felina.',
            'year': 2021,
            'genre': 'Feline-thriller',
            'category': 'movie',
            'poster_url': 'https://placekitten.com/300/450?image=28',
            'video_url': 'https://example.com/video28',
        },
        {
            'title': 'Risadas Felinas ao Entardecer',
            'description': 'Uma sitcom sobre a vida hilariante de três gatos apartados.',
            'year': 2024,
            'genre': 'Cat-edy',
            'category': 'series',
            'poster_url': 'https://placekitten.com/300/450?image=29',
            'video_url': 'https://example.com/video29',
        },
        {
            'title': 'O Santuário Secreto dos Gatos',
            'description': 'Um documentário explorando o mundo oculto de gatos selvagens.',
            'year': 2023,
            'genre': 'Purr-drama',
            'category': 'documentary',
            'poster_url': 'https://placekitten.com/300/450?image=30',
            'video_url': 'https://example.com/video30',
        },
    ]
    
    def handle(self, *args, **options):
        """Execute the seeding command."""
        
        # Check if movies already exist
        if Movie.objects.exists():
            self.stdout.write(
                self.style.WARNING('Movies already exist in database. Skipping seed.')
            )
            return
        
        # Create movies
        movies = [Movie(**movie_data) for movie_data in self.CAT_MOVIES]
        Movie.objects.bulk_create(movies)
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully seeded {len(self.CAT_MOVIES)} cat-themed movies!'
            )
        )
