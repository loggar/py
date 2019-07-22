# django

ref)

- https://docs.djangoproject.com/en/2.2/intro

## Custom view

when you add views for polls application:

`polls/views.py`

```py
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

add url patterns:

`polls/urls.py`

```py
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

index response with output:

`polls/views.py`

```py
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```

or render the templates:

`polls/views.py`

```py
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# Leave the rest of the views (detail, results, vote) unchanged
```

`polls/templates/polls/index.html`

```html
{% if latest_question_list %}
<ul>
  {% for question in latest_question_list %}
  <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
  {% endfor %}
</ul>
{% else %}
<p>No polls are available.</p>
{% endif %}
```

a shortcut for render: using `render()`

`polls/views.py`

```py
from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Leave the rest of the views (detail, results, vote) unchanged
```

```
$ python manage.py runserver

# http://127.0.0.1:8000/polls/
# http://127.0.0.1:8000/polls/1/
```

### raising a 404 error

`polls/views.py`

```py
from django.http import Http404

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
```

`polls/templates/polls/detail.html`

```html
<h1>{{ question.question_text }}</h1>
<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }}</li>
  {% endfor %}
</ul>
```

a shortcut for 404: `get_object_or_404()`

`polls/views.py`

```py
from django.shortcuts import get_object_or_404, render

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

### Removing hardcoded URLs in templates

`polls/views.py`

```py
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

`polls/urls.py`

```py
path('specifics/<int:question_id>/', views.detail, name='detail'),
```

### Namespacing URL names

`polls/urls.py`

```py
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

`polls/templates/polls/index.html`

```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

## form

`polls/templates/polls/detail.html`

```html
<h1>{{ question.question_text }}</h1>

{% if error_message %}
<p>
  <strong>{{ error_message }}</strong>
</p>
{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
  {% csrf_token %} {% for choice in question.choice_set.all %}
  <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
  <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
  {% endfor %}
  <input type="submit" value="Vote" />
</form>
```

`polls/views.py`

```py
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

`polls/templates/polls/results.html`

```html
<h1>{{ question.question_text }}</h1>

<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes | pluralize }}</li>
  {% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

## Generic Views

`polls/urls.py`

```py
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
