# django

## Django module

```
$ pip install django

$ python -m django --version
```

## init with django-admin

```
$ django-admin startproject startedproject

$ cd startedproject
```

Change dbfile path:

`startedproject/settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '_tmp', 'db.sqlite3'),
    }
}
```

## run server

```
$ python manage.py runserver
```

Changing the port

```
python manage.py runserver 8080
```

Changing the host

```
python manage.py runserver 0.0.0.0:8000
```

## Creating the "Polls" app

```
python manage.py startapp polls
```

### view

`polls/views.py`

```py
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

```

`polls/urls.py`

```py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

`startedproject/urls.py`

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

When to use `include()`

- You should always use `include()` when you include other URL patterns. admin.site.urls is the only exception to this.

Restart server

```
$ python manage.py runserver

# http://127.0.0.1:8000/polls/
# http://127.0.0.1:8000/admin/
```

### `path()` argument

- route
- view
- kwargs
- name
