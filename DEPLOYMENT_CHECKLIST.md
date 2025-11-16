🚀 Checklist de Deploy – GatoFlix
🧪 Testes antes do deploy (ambiente local)
Segurança

 Rodar os testes: python manage.py test — tudo deve passar

 Testar com DEBUG=False localmente

 Gerar um SECRET_KEY novo:

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


 Testar limite de tentativas de login (6 tentativas rápidas deve travar)

 Confirmar que senhas fracas são rejeitadas

 Validar senha forte (ex: Strong123)

 Verificar headers de segurança com DEBUG desativado

Banco de Dados

 Backup do banco SQLite (se necessário)

 Rodar migrations: python manage.py migrate

 Se desejar, popular com dados iniciais: python manage.py seed_cats

 Testar os endpoints da API em localhost

Logs

 Criar a pasta logs/ (ou verificar se o Django cria sozinho)

 Verificar se gatoflix.log e auth.log estão sendo escritos

🌐 Deploy no Render
1. Variáveis de ambiente

No painel do Render, configurar:

SECRET_KEY=<gerado anteriormente>
DEBUG=False
ALLOWED_HOSTS=<seu-app>.onrender.com
CORS_ALLOWED_ORIGINS=https://<frontend>.vercel.app
DATABASE_URL=<definido pelo Render>

2. Itens críticos pra conferir

 SECRET_KEY novo

 DEBUG=False

 ALLOWED_HOSTS preenchido com domínio do Render

 CORS_ALLOWED_ORIGINS com domínio do frontend

3. Arquivos de build

 build.sh com permissão de execução

 Procfile com o comando correto

 .gitignore ignorando db.sqlite3, .env, *.pyc

4. Banco de Dados no Render

 PostgreSQL conectado

 Leitura do DATABASE_URL com dj-database-url

 Rodar migrations via build ou console do Render

5. Depois de publicado

 Acessar logs no Render (procurar erros)

 Testar /movies/

 Testar /auth/register/ e /auth/login/

 Confirmar CORS funcionando

 Conferir headers de segurança

📊 Monitoramento pós-deploy
Monitoramento

 Usar um serviço de uptime (ex: UptimeRobot)

 Testar tempo de resposta da API

 Ver logs com frequência

 Verificar tentativas de login no auth.log

 Configurar alerta para erros 5XX

Performance

 Resposta do endpoint em <500ms

 Queries otimizadas

 Arquivos estáticos servidos por WhiteNoise

🔐 Checagem de segurança após deploy
Itens essenciais

 HTTPS funcional

 Header HSTS ativo

 X-Frame-Options configurado

 X-Content-Type-Options ativado

 CSP configurado

 Rate limiting funcionando (testar via curl)

Testes rápidos
curl https://<app>.onrender.com/movies/


Teste limite:

for i in {1..6}; do
  curl -X POST https://<app>.onrender.com/auth/register/ \
    -H "Content-Type: application/json" \
    -d '{"username":"teste'$i'","email":"teste'$i'@teste.com","password":"Teste123","password_confirm":"Teste123"}'
done


Login:

curl -X POST https://<app>.onrender.com/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test1","password":"Teste123"}'

🛠️ Problemas comuns
502 Bad Gateway

Verifique logs do Render

Conferir SECRET_KEY

DEBUG=False configurado corretamente

Migrations rodadas

CORS

Checar CORS_ALLOWED_ORIGINS

Conferir domínio do frontend

Limpar cache do navegador

401 Unauthorized

Conferir JWT retornando

Header com "Bearer <token>"

Configuração do SIMPLE_JWT

Erro no banco

DATABASE_URL definida

psycopg2-binary listado no requirements.txt

Fazer deploy forçado (Force Deploy)

🔄 Plano de rollback

Se der problema:

Rollback para o commit anterior

Ver logs detalhados do Render

Corrigir e fazer novo deploy

Banco: o Render faz backups automáticos

🟢 Sinal de sucesso

Depois do deploy, você deve ver:

/movies/ respondendo

Dominio HTTPS ok

Headers de segurança funcionando

Limite de requisições ativo

Logs sendo gerados

Resposta da API em menos de 1s

💡 Comandos úteis
# Rodar com DEBUG=False localmente
DEBUG=False python manage.py runserver

# Gerar nova SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Rodar testes
python manage.py test --verbosity=2

# Verificar configurações de deploy
python manage.py check --deploy

# Criar superuser
python manage.py createsuperuser

📞 Suporte

Se tiver problemas:

Verifique o status do Render (render.com/status)

Consulte os arquivos de documentação (SECURITY_UPDATES.md, etc)

Cheque versões em requirements.txt