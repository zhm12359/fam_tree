from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    big = models.CharField(max_length=200)
    assistant_big = models.CharField(max_length=200)
    big_2 = models.CharField(max_length=200)
    assistant_big_2 = models.CharField(max_length=200)

