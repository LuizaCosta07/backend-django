🐾 GatoFlix – Backend API

API REST feita com Django e Django REST Framework, inspirada no universo dos gatos. Ideal para ser usada com um frontend (React, Vue, etc.).

✨ Funcionalidades

Autenticação JWT (JSON Web Token)

Sistema de favoritos por usuário

Filtros (search, genre, year, category) e paginação em filmes

Deploy pronto para Render/Heroku

Uso de banco SQLite (local) e PostgreSQL (produção)

Admin estilizado com tema felino

📌 Tecnologias Principais
Categoria	Tecnologia
Linguagem	Python 3.10+
Framework	Django 5
API	Django REST Framework
Autenticação	SimpleJWT
Banco de Dados	PostgreSQL (produção) / SQLite (local)
Servidor	Gunicorn + WhiteNoise
🚀 Rodando o Projeto Localmente
1. Clonagem e Configuração Inicial
git clone <url-do-repositório>
cd gatoflix

2. Ambiente Virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

3. Instalação de Dependências
pip install -r requirements.txt

4. Variáveis de Ambiente (.env)

Crie o arquivo .env na raiz do projeto:

SECRET_KEY=sua-chave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL (produção - opcional para local)
DATABASE_URL=

# Liberação do Frontend
CORS_ALLOWED_ORIGINS=http://localhost:3000

5. Banco de Dados e Usuário
python manage.py migrate
python manage.py seed_cats   # (Opcional) Popula com 30 filmes
python manage.py createsuperuser

6. Início do Servidor
python manage.py runserver


Acesse em: http://localhost:8000

💻 Endpoints da API
Autenticação
Ação	Endpoint	Método
Registrar usuário	/auth/register/	POST
Login	/auth/login/	POST
Ver perfil	/auth/me/	GET

Use o cabeçalho:
Authorization: Bearer <token_jwt>

Filmes
GET /movies/?search=gato&genre=Cat-edy&year=2023&category=movie&page=1

Parâmetro	Descrição
search	Busca por título ou descrição
genre	Filtra pelo gênero (ex: Cat-edy)
year	Filtra pelo ano
category	Filtra por tipo (movie, series, etc.)
page	Controla a paginação
Favoritos
Ação	Endpoint	Método
Listar favoritos	/favorites/	GET
Adicionar favorito	/favorites/<movie_id>/add/	POST
Remover favorito	/favorites/<movie_id>/remove/	DELETE
📂 Estrutura do Projeto
gatoflix/
├── gatoflix/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
├── movies/
├── favorites/
├── manage.py
├── requirements.txt
├── Procfile
└── build.sh

☁️ Deploy no Render
Configuração	Valor
Build Command	bash build.sh
Start Command	gunicorn gatoflix.wsgi

Suba o código no GitHub

Crie um Web Service no Render

Configure os comandos acima

Defina as variáveis de ambiente (SECRET_KEY, DEBUG=False,DATABASE_URL, etc.)

Faça o deploy 🚀

🧪 Exemplo de Teste com curl
Login
curl -X POST http://localhost:8000/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"miau","password":"123456"}'

Listar Filmes
curl http://localhost:8000/movies/

👩‍💻 Integração com Frontend
const token = localStorage.getItem("access");

fetch("https://seu-backend.com/favorites/", {
  headers: {
    Authorization: `Bearer ${token}`,
  },
});

🐈 Temática GatoFlix

Filmes como O Gato das Sombras, Whisker Wars, etc.

Gêneros como Cat-edy, Meow-horror, Whisker-sci-fi

Seed automático com 30 filmes

Admin com tema felino 🐾

📞 Contato

Dúvidas ou problemas?
Abra uma issue aqui no repositório.
😺 Estamos prontos para te ajudar!
