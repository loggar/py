# django

## style

`polls/static/polls/style.css`

```css
body {
  background: #eeeeee;
}

li a {
  color: green;
}
```

`polls templates`:

```html
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
```
