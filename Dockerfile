FROM python:3.11-alpine

RUN mkdir test_gurtam
WORKDIR /test_gurtam

COPY requirements.txt .

RUN pip install --upgrade pip
RUN apk add --no-cache postgresql-dev gcc musl-dev
RUN pip install -r requirements.txt

COPY . /test_gurtam

COPY cronjobs /etc/cron.d/cronjobs
RUN chmod 0744 /etc/cron.d/cronjobs
RUN crontab /etc/cron.d/cronjobs

CMD until nc -z -v -w30 postgres-db 5432; do echo "Waiting for database connection..."; sleep 1; done \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py shell -c "import os; \
                                   from django.contrib.auth import get_user_model; \
                                   User = get_user_model(); \
                                   User.objects.create_superuser(os.getenv('DJANGO_SUPERUSER_USERNAME'), os.getenv('DJANGO_SUPERUSER_EMAIL'), os.getenv('DJANGO_SUPERUSER_PASSWORD'))" \
    && python manage.py collectstatic --noinput \
    && gunicorn test_gurtam.wsgi:application --bind 0.0.0.0:8000 \
    && cron -f