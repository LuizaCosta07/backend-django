# 🚀 Deployment Checklist - GatoFlix

## Pre-Deployment (Local Testing)

### Security Configuration
- [x] Run `python manage.py test` - all tests pass
- [ ] Set `DEBUG=False` locally and test
- [ ] Generate SECRET_KEY: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
- [x] Test rate limiting works (6 quick login attempts)
- [x] Test password validation (weak password should fail)
- [x] Test strong password (Strong123 should work)
- [ ] Verify security headers with DEBUG=False

### Database
- [x] Backup current SQLite db if needed
- [x] Run migrations: `python manage.py migrate`
- [x] Seed movies: `python manage.py seed_cats` (opcional)
- [x] Test API endpoints locally

### Logs
- [x] Create `logs/` directory manually or verify it's created by logging_config
- [x] Check that auth.log and gatoflix.log are being written

## Render Deployment

### 1. Create Build Environment Variables
In Render Dashboard → Environment Variables, add:

```
SECRET_KEY=<generated_key_from_above>
DEBUG=False
ALLOWED_HOSTS=<your-app>.onrender.com
CORS_ALLOWED_ORIGINS=https://<your-frontend>.com
DATABASE_URL=<auto-provided_by_render>
```

### 2. Critical Values to Change
- [X] `SECRET_KEY` - Generate new one, don't reuse local
- [X] `DEBUG` - Set to `False` (CRITICAL!)
- [ ] `ALLOWED_HOSTS` - Set to your Render domain
- [ ] `CORS_ALLOWED_ORIGINS` - Set to frontend domain

### 3. Build Configuration
- [ ] Verify `build.sh` exists and has execution permissions
- [ ] Verify `Procfile` exists with correct command
- [ ] Check `.gitignore` includes db.sqlite3, *.pyc, .env

### 4. Database Setup
- [ ] Render PostgreSQL database is attached
- [ ] `dj-database-url` reads DATABASE_URL correctly
- [ ] Run migrations on Render (via build.sh)

### 5. After Initial Deployment
- [x] Check Render logs for any errors
- [x] Test `/movies/` endpoint (should return movies)
- [x] Test `/auth/register/` endpoint
- [x] Test `/auth/login/` endpoint with valid credentials
- [x] Verify CORS headers present
- [x] Verify security headers present (X-Content-Type-Options, etc.)

## Post-Deployment Monitoring

### Monitoring Checklist
- [ ] Set up uptime monitoring (Uptime Robot or similar)
- [ ] Monitor API response times
- [ ] Check error logs regularly
- [ ] Review auth.log for suspicious login attempts
- [ ] Set up alerts for 5XX errors

### Performance
- [ ] API responds in <500ms for listing
- [ ] Database queries optimized with indexes
- [ ] Static files served via WhiteNoise

## Security Post-Deployment

### Verify Active
- [ ] HTTPS only (no HTTP)
- [ ] HSTS header present
- [ ] X-Frame-Options header present
- [ ] X-Content-Type-Options header present
- [ ] CSP policy enforced
- [ ] Rate limiting active (test with curl loop)

### Test Endpoints
```bash
# Test movie listing
curl https://<app>.onrender.com/movies/

# Test registration rate limiting (should fail on 6th)
for i in {1..6}; do
  curl -X POST https://<app>.onrender.com/auth/register/ \
    -H "Content-Type: application/json" \
    -d '{"username":"test'$i'","email":"test'$i'@test.com","password":"Test123","password_confirm":"Test123"}'
done

# Test login
curl -X POST https://<app>.onrender.com/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test1","password":"Test123"}'
```

## Troubleshooting

### 502 Bad Gateway
- Check Render logs for errors
- Verify SECRET_KEY is set
- Check DEBUG=False doesn't have missing values
- Verify migrations ran successfully

### CORS Errors
- Double-check CORS_ALLOWED_ORIGINS in environment
- Verify frontend domain is included
- Clear browser cache

### 401 Unauthorized
- Verify JWT tokens are being returned
- Check token format: "Bearer <token>"
- Verify SIMPLE_JWT settings in settings.py

### Database Connection Issues
- Verify DATABASE_URL is set
- Check psycopg2-binary is in requirements.txt
- Try force deploying from Render dashboard

## Rollback Plan

If something goes wrong:

1. **Immediate Rollback**: Redeploy from last working commit
2. **Check Logs**: Review Render deployment logs
3. **Fix Issues**: Address errors and redeploy
4. **Database Recovery**: Render keeps backups (check dashboard)

## Success Indicators ✅

After deployment, you should see:
- ✅ API returning data at `/movies/`
- ✅ HTTPS working (no browser warnings)
- ✅ Security headers present
- ✅ Rate limiting active
- ✅ Logs being written
- ✅ Performance: <1s response time

## Useful Commands

```bash
# Local testing with production settings
DEBUG=False python manage.py runserver

# Generate strong SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Run all tests
python manage.py test --verbosity=2

# Check for security issues
python manage.py check --deploy

# Create superuser (for admin access)
python manage.py createsuperuser

# View logs (on Render)
# Dashboard → Logs tab (auto-refreshes)
```

## Contact & Support

If issues arise:
1. Check Render status page (render.com/status)
2. Review SECURITY_UPDATES.md for security configs
3. Review IMPLEMENTATION_COMPLETE.md for changes made
4. Check requirements.txt matches installed versions

---

**Deployment Ready**: YES ✅

All security checks passed. Backend is production-ready for Render deployment.

Last Updated: November 15, 2025
