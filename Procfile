release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn kapos_prj.wsgi --workers 1 --threads 2 --timeout 90 --max-requests 80
