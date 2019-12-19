"""
A BooleanField in Django accepts only the two values: true and false. If you need to accept NULL values, you have to use a NullBooleanField.

Anti-pattern:

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    activated = models.BooleanField(null=True)
"""

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # Using NullBooleanField instead
    activated = models.NullBooleanField()
