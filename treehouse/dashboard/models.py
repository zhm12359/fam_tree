from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    big = models.CharField(max_length=200, blank=True, default='')
    assistant_big = models.CharField(max_length=200, blank=True, default='')
    big_2 = models.CharField(max_length=200, blank=True, default='')
    assistant_big_2 = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        unique_together = ('name', 'big',)

    def __str__(self):
        return self.name;

