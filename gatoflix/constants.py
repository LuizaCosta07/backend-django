"""
API Response structure and standard formats for GatoFlix.

Standard JSON Response Format:
{
  "status": "success|error",
  "data": {...},
  "message": "Optional message"
}

Pagination Format:
{
  "count": 100,
  "next": "http://...",
  "previous": "http://...",
  "results": [...]
}

Error Response:
{
  "detail": "Error message"
}
"""

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

RESPONSE_MESSAGES = {
    'success': 'Operação realizada com sucesso.',
    'created': 'Recurso criado com sucesso.',
    'updated': 'Recurso atualizado com sucesso.',
    'deleted': 'Recurso removido com sucesso.',
    'not_found': 'Recurso não encontrado.',
    'unauthorized': 'Autenticação necessária.',
    'forbidden': 'Acesso negado.',
    'invalid': 'Dados inválidos.',
}
