# 🐾 GatoFlix Backend API

Backend REST API Django/DRF para GatoFlix - Plataforma de Streaming Temática de Gatos com autenticação JWT, favoritos, filtros, paginação e deploy no Render.

## 📋 Requisitos

- Python 3.10+
- pip
- virtualenv (recomendado)

## 🚀 Instalação Local (5 minutos)

### 1. Clone e Configure

```bash
cd gatoflix
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 2. Instale Dependências

```bash
pip install -r requirements.txt
```

### 3. Crie o Banco de Dados

```bash
python manage.py migrate
```

### 4. (Opcional) Popular com 30 Filmes de Gatos

```bash
python manage.py seed_cats
```

### 5. Crie um Superuser (para admin)

```bash
python manage.py createsuperuser
```

### 6. Inicie o Servidor

```bash
python manage.py runserver
```

Acesse em `http://localhost:8000`

## 📚 Endpoints da API

### 🔐 Autenticação

#### Registrar
```
POST /auth/register/

Body:
{
  "username": "usuario",
  "email": "user@example.com",
  "password": "senha123",
  "password_confirm": "senha123"
}

Response (201):
{
  "user": {"id": 1, "username": "usuario", "email": "user@example.com", ...},
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### Login
```
POST /auth/login/

Body:
{
  "username": "usuario",
  "password": "senha123"
}

Response (200): Mesmo formato do register
```

#### Usuário Atual
```
GET /auth/me/

Headers:
Authorization: Bearer <access_token>

Response (200):
{
  "id": 1,
  "username": "usuario",
  "email": "user@example.com",
  "first_name": "Nome",
  "last_name": "Sobrenome"
}
```

### 🎬 Filmes

#### Listar Filmes
```
GET /movies/?search=gato&genre=Feline-thriller&year=2023&page=1

Query Parameters:
- search: Buscar em título/descrição
- genre: Feline-thriller, Cat-edy, Purr-drama, Whisker-sci-fi, Paw-western, Meow-horror, Kitten-romance, Tiger-action
- year: Ano de lançamento
- category: movie, series, documentary
- page: Página (padrão: 1, 10 itens/página)

Response (200):
{
  "count": 30,
  "next": "http://localhost:8000/movies/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "O Gato das Sombras",
      "description": "Um gato misterioso viaja através do tempo...",
      "year": 2023,
      "genre": "Feline-thriller",
      "category": "movie",
      "poster_url": "https://placekitten.com/300/450?image=1",
      "video_url": "https://example.com/video1",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

#### Detalhes do Filme
```
GET /movies/<id>/

Response (200): Mesmo formato acima + updated_at
```

### ❤️ Favoritos

#### Listar Favoritos
```
GET /favorites/?page=1

Headers:
Authorization: Bearer <access_token>

Response (200):
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "movie": {...},
      "created_at": "2024-01-15T11:00:00Z"
    }
  ]
}
```

#### Adicionar aos Favoritos
```
POST /favorites/<movie_id>/add/

Headers:
Authorization: Bearer <access_token>

Response (201): Retorna o objeto Favorite criado
```

#### Remover dos Favoritos
```
DELETE /favorites/<movie_id>/remove/

Headers:
Authorization: Bearer <access_token>

Response (204): No Content
```

## 📁 Estrutura do Projeto

```
gatoflix/
├── gatoflix/
│   ├── settings.py          # Configurações Django
│   ├── urls.py              # URLs principais
│   ├── wsgi.py              # WSGI
│   ├── admin.py             # Admin customizado
│   ├── cors_config.py       # Config CORS
│   ├── constants.py         # Constantes
│   └── __init__.py
├── movies/
│   ├── models.py            # Modelo Movie
│   ├── serializers.py       # Serializers
│   ├── views.py             # ViewSets
│   ├── urls.py              # URLs
│   ├── admin.py             # Admin customizado
│   ├── apps.py
│   ├── management/commands/seed_cats.py
│   ├── migrations/
│   └── __init__.py
├── accounts/
│   ├── serializers.py       # Auth serializers
│   ├── views.py             # Register/Login/Me
│   ├── urls.py              # URLs
│   ├── apps.py
│   ├── migrations/
│   └── __init__.py
├── favorites/
│   ├── models.py            # Modelo Favorite
│   ├── serializers.py       # Serializers
│   ├── views.py             # ViewSet
│   ├── urls.py              # URLs
│   ├── admin.py             # Admin customizado
│   ├── apps.py
│   ├── migrations/
│   └── __init__.py
├── manage.py
├── requirements.txt
├── .env.example
├── Procfile
├── build.sh
└── README.md
```

## 🔧 Configuração (.env)

Crie arquivo `.env` na raiz:

```env
SECRET_KEY=sua-chave-secreta-super-segura
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database (deixe em branco para SQLite local)
DATABASE_URL=

# CORS para frontend React
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000,https://yourdomain.com
```

## 🚀 Deploy no Render

### 1. Push para GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <seu-repo>
git push -u origin main
```

### 2. No Render Dashboard

1. Clique em "New +" → "Web Service"
2. Conecte seu repositório GitHub
3. Configure:
   - **Build Command**: `bash build.sh`
   - **Start Command**: `gunicorn gatoflix.wsgi`

### 3. Variáveis de Ambiente (no dashboard)

```
SECRET_KEY=<gere-uma-nova-chave-segura>
DEBUG=False
ALLOWED_HOSTS=seu-app.onrender.com
CORS_ALLOWED_ORIGINS=https://seu-frontend.com
DATABASE_URL=<Render fornecerá automaticamente>
```

### 4. Criar Banco PostgreSQL

1. No Render: "New +" → "PostgreSQL"
2. Copie a `DATABASE_URL`
3. Adicione na variável de ambiente do Web Service
4. Deploy fará as migrations automaticamente

O site estará live em `https://seu-app.onrender.com`

## 🧪 Testes com curl

```bash
# Registrar
curl -X POST http://localhost:8000/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","email":"test@example.com","password":"123456","password_confirm":"123456"}'

# Login
curl -X POST http://localhost:8000/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"123456"}'

# Listar filmes
curl http://localhost:8000/movies/

# Adicionar aos favoritos (com token)
curl -X POST http://localhost:8000/favorites/1/add/ \
  -H "Authorization: Bearer <seu-token>"
```

## 🐾 Temas GatoFlix

Todos os filmes e dados são temáticos com gatos:

- **Títulos**: "O Gato das Sombras", "Gatadas: O Retorno", "Ronrom: Uma História de Amor", etc.
- **Gêneros**: Feline-thriller, Cat-edy, Purr-drama, Whisker-sci-fi, Paw-western, Meow-horror, Kitten-romance, Tiger-action
- **Admin**: "GatoFlix Admin 🐾"
- **Posters**: placekitten.com (gatos aleatórios)

## 🔒 Segurança

- JWT com expiração 24h (access) e 7 dias (refresh)
- Senhas hasheadas PBKDF2
- CORS restrito a domínios específicos
- WhiteNoise para arquivos estáticos
- SQL injection prevention via ORM Django
- ALLOWED_HOSTS configurável

## 📦 Dependências Principais

- Django 5.0
- Django REST Framework 3.14
- SimpleJWT 5.3.2 (autenticação JWT)
- django-cors-headers 4.3
- dj-database-url 2.1 (suporte PostgreSQL)
- python-dotenv 1.0 (variáveis de ambiente)
- gunicorn 21.2 (WSGI server)
- whitenoise 6.6 (arquivos estáticos)
- psycopg2-binary 2.9 (driver PostgreSQL)

## 📖 Features Implementadas

✅ Autenticação JWT com register/login  
✅ 30 filmes temáticos de gatos (comando seed)  
✅ Filtros: search, genre, year, category  
✅ Paginação: 10 itens/página  
✅ Favoritos com UNIQUE constraint  
✅ CORS configurável via env  
✅ Admin customizado com "GatoFlix Admin 🐾"  
✅ SQLite (local) + PostgreSQL (Render)  
✅ WhiteNoise para produção  
✅ Build script para Render  
✅ Variáveis de ambiente seguras  

## 🤝 Para Conectar com React Frontend

1. **Instale em seu projeto React**:
```bash
npm install axios
```

2. **Use a API**:
```javascript
const BASE_URL = 'http://localhost:8000';

// Registrar
const response = await fetch(`${BASE_URL}/auth/register/`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'user',
    email: 'user@example.com',
    password: 'senha123',
    password_confirm: 'senha123'
  })
});
const { access, refresh } = await response.json();
localStorage.setItem('access_token', access);

// Login
const loginResponse = await fetch(`${BASE_URL}/auth/login/`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ username: 'user', password: 'senha123' })
});

// Usar token em requisições
fetch(`${BASE_URL}/favorites/`, {
  headers: { 'Authorization': `Bearer ${localStorage.getItem('access_token')}` }
});
```

3. **Configure CORS** (já vem pronto, apenas ajuste `.env` com seu frontend URL)

## 📝 Documentação Completa

Veja as respostas JSON dos endpoints acima. A API segue padrão REST com paginação automática.

## 🐛 Troubleshooting

| Erro | Solução |
|------|---------|
| `ModuleNotFoundError: django` | `pip install -r requirements.txt` |
| `relation does not exist` | `python manage.py migrate` |
| CORS bloqueado | Ajuste `CORS_ALLOWED_ORIGINS` em `.env` |
| `No such table` | `python manage.py migrate && python manage.py seed_cats` |

## 📞 Suporte

Para bugs ou dúvidas, abra uma issue no repositório.

---

**🐾 Feito com ❤️ para amantes de gatos**
