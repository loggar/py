# django

ref)

- https://docs.djangoproject.com/en/2.2/intro

## Database setup

`startedproject/settings.py`

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '_tmp', 'db.sqlite3'),
    }
}
```

```py
TIME_ZONE = 'UTC'
```

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Some of these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:

```
$ python manage.py migrate
```

### models

Creating Models

`polls/models.py`

```py
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Activating Model

`startedproject/settings.py`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig',
]
```

```
$ python manage.py makemigrations polls
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" integer NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```

This checks for any problems in your project without making migrations or touching the database:

```
$ python manage.py check
```

Now, run migrate again to create those model tables in your database:

```
$ python manage.py migrate
```

## palying with the API

Python shell

```
$ python manage.py shell

In [1]: from polls.models import Choice, Question

In [2]: Question.objects.all()
Out[2]: <QuerySet []>

In [3]: from django.utils import timezone

In [4]: q = Question(question_text="What's new?", pub_date=timezone.now())

In [5]: q.save()

In [6]: q.id
Out[6]: 1

In [7]: q.question_text
Out[7]: "What's new?"

In [8]: q.pub_date
Out[8]: datetime.datetime(2019, 7, 22, 2, 5, 21, 869852, tzinfo=<UTC>)

In [9]: q.question_text = "What's up?"

In [10]: q.save()

In [11]: Question.objects.all()
Out[11]: <QuerySet [<Question: Question object (1)>]>
```

`<Question: Question object (1)>` isn’t a helpful representation of this object. Let’s fix that by editing the Question model (in the `polls/models.py` file) and adding a `__str__()` method to both Question and Choice:

`polls/models.py`

```py
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

```
$ python manage.py shell

In [1]: from polls.models import Choice, Question

In [2]: Question.objects.all()
Out[2]: <QuerySet [<Question: What's up?>]>

In [3]: Question.objects.filter(id=1)
Out[3]: <QuerySet [<Question: What's up?>]>

In [4]: Question.objects.filter(question_text__startswith='What')
Out[4]: <QuerySet [<Question: What's up?>]>

In [5]: from django.utils import timezone

In [6]: current_year = timezone.now().year

In [7]: Question.objects.get(pub_date__year=current_year)
Out[7]: <Question: What's up?>

In [8]: Question.objects.get(pk=1)
Out[8]: <Question: What's up?>

In [9]: q = Question.objects.get(pk=1)

In [10]: q.was_published_recently()
Out[10]: True

In [11]: q.choice_set.all()
Out[11]: <QuerySet []>

In [12]: q.choice_set.create(choice_text='Not much', votes=0)
Out[12]: <Choice: Not much>

In [13]: q.choice_set.create(choice_text='The sky', votes=0)
Out[13]: <Choice: The sky>

In [14]: c = q.choice_set.create(choice_text='Just hacking again', votes=0)

In [15]: c.question
Out[15]: <Question: What's up?>

In [16]: q.choice_set.all()
Out[16]: <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

In [17]: q.choice_set.count()
Out[17]: 3

In [18]: Choice.objects.filter(question__pub_date__year=current_year)
Out[18]: <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

In [19]: c = q.choice_set.filter(choice_text__startswith='Just hacking')

In [20]: c.delete()
Out[20]: (1, {'polls.Choice': 1})

In [21]: Question.objects.all()
Out[21]: <QuerySet [<Question: What's up?>]>
```
