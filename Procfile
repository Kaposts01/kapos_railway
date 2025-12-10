release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn kapos_prj.wsgi --timeout 120 --workers 1 --threads 1
