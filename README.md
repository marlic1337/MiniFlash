MiniFlash
=========

Minimalistic agile development tool

Dependencies:
    Django==1.6.7
    South==1.0
    django-allauth==0.18.0
    django-bootstrap3==4.11.0
    oauthlib==0.6.3
    pil==1.1.7
    psycopg2==2.5.4
    python-openid==2.2.5
    requests==2.4.1
    requests-oauthlib==0.4.1

Schema migrations:
	When you create a new app with models: python manage.py schemamigration APPNAME --initial; python manage.py migrate
	When you modify models.py: python manage.py schemamigration APPNAME --auto; python manage.py migrate
	When you git pull new migrations: python manage.py migrate

Superuser account:
    Username: admin,
    Email: admin@admin.com,
    Password: admin