🐾 GatoFlix - API Backend

Este é o backend da plataforma GatoFlix, uma aplicação temática de streaming 100% inspirada no universo dos gatos. Foi desenvolvido com Django e Django REST Framework e conta com autenticação JWT, sistema de favoritos, filtros, paginação e pronto para deploy na plataforma Render.

📋 Pré-requisitos

Python 3.10 ou superior

pip atualizado

virtualenv (opcional, mas recomendado)

🚀 Como rodar o projeto localmente
1. Clonar o repositório e ativar o ambiente virtual
git clone <url-do-repo>
cd gatoflix
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

2. Instalar as dependências
pip install -r requirements.txt

3. Configurar o banco de dados e rodar as migrations
python manage.py migrate

4. (Opcional) Popular o banco com filmes temáticos
python manage.py seed_cats

5. Criar um usuário admin
python manage.py createsuperuser

6. Rodar o servidor local
python manage.py runserver


A API estará disponível em:
📍 http://localhost:8000

📚 Endpoints Principais
🔐 Autenticação
Registrar usuário

POST /auth/register/

{
  "username": "usuario",
  "email": "user@example.com",
  "password": "senha123",
  "password_confirm": "senha123"
}


Retorna um token access e refresh.

Login

POST /auth/login/

{
  "username": "usuario",
  "password": "senha123"
}

Recuperar dados do usuário autenticado

GET /auth/me/
Header: Authorization: Bearer <token>

🎬 Filmes (com filtros e paginação)
Listar filmes

GET /movies/?search=gato&genre=Feline-thriller&year=2023&page=1

Filtros disponíveis:

search: busca por título/descrição

genre: gênero temático

year: ano de lançamento

category: movie, series, documentary

page: paginação (10 itens por página)

❤️ Favoritos
Listar favoritos

GET /favorites/
Header: Authorization: Bearer <token>

Adicionar um filme aos favoritos

POST /favorites/<movie_id>/add/

Remover dos favoritos

DELETE /favorites/<movie_id>/remove/

🗂️ Estrutura do projeto
gatoflix/
├── gatoflix/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── cors_config.py
│   └── ...
├── movies/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── management/commands/seed_cats.py
│   └── ...
├── accounts/
├── favorites/
├── manage.py
├── requirements.txt
├── build.sh
└── Procfile

🔧 Configuração com .env

Crie um arquivo .env na raiz com:

SECRET_KEY=sua-chave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,seu-app.onrender.com

# Para PostgreSQL em produção (opcional)
DATABASE_URL=

# Liberação do frontend (React ou outro)
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://seu-frontend.com

🚀 Deploy na Render
1. Envie o código para o GitHub
git init
git add .
git commit -m "Deploy inicial"
git remote add origin <url-do-repo>
git push -u origin main

2. No Render:

Crie um novo Web Service

Configure assim:

Build Command: bash build.sh

Start Command: gunicorn gatoflix.wsgi

3. Adicione as variáveis de ambiente:
SECRET_KEY=gera-uma-chave
DEBUG=False
ALLOWED_HOSTS=seu-app.onrender.com
CORS_ALLOWED_ORIGINS=https://seu-frontend.com
DATABASE_URL=<Render gera automaticamente>

4. Conecte um banco PostgreSQL (opcional)

Render → "New +" → PostgreSQL → copie o DATABASE_URL e coloque nas env.

💻 Testando com curl
# Cadastro
curl -X POST http://localhost:8000/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"miau","email":"miau@example.com","password":"123456","password_confirm":"123456"}'

# Login
curl -X POST http://localhost:8000/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"miau","password":"123456"}'

# Listar filmes
curl http://localhost:8000/movies/

🐾 Temática GatoFlix

Filmes com nomes como: “O Gato das Sombras”, “Ronrom: Uma História de Amor”

Gêneros felinos: Cat-edy, Meow-horror, Whisker-sci-fi, etc.

Mini seed automático com 30 filmes

Painel admin estilizado com tema felino 🐱

🔒 Segurança

Autenticação com JWT (access e refresh)

Senhas seguradas com PBKDF2

CORS configurável

Deploy com WhiteNoise para arquivos estáticos

Banco SQLite local / PostgreSQL no Render

📦 Principais dependências

Django 5

DRF 3.14

SimpleJWT

django-cors-headers

dj-database-url

gunicorn

whitenoise

psycopg2-binary

🤝 Integração com React

Basta fazer requests para os endpoints e usar o token JWT no header. Exemplo:

const token = localStorage.getItem('access');

fetch('https://seu-backend.com/favorites/', {
  headers: {
    Authorization: `Bearer ${token}`
  }
});

🐛 Dicas para correção de erros
Erro	Solução
django não encontrado	pip install -r requirements.txt
No such table	Rodar python manage.py migrate
CORS bloqueado	Ajustar o CORS_ALLOWED_ORIGINS no .env
500 no Render	Conferir logs e SECRET_KEY
📞 Suporte

Ficou com dúvidas ou achou algum problema?
Abra uma issue no repositório ou me chame — será um prazer ajudar 🐱