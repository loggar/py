# django

ref)

- https://docs.djangoproject.com/en/2.2/intro

## Introducing the Django Admin

```
$ python manage.py createsuperuser

Username (leave blank to use 'webnl'): admin
Email address: admin@example.com
Password: admin1234$#@!
Password (again): admin1234$#@!
Superuser created successfully.
```

Start the development server:

```
$ python manage.py runserver
```

```
$ python manage.py runserver

# http://127.0.0.1:8000/admin/
```

### Make the poll app modifiable in the admin

`polls/admin.py`

```py
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
