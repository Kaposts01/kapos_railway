release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn kapos_prj.wsgi --workers 1 --threads 1 --timeout 120 --max-requests 120
