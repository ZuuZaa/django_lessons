from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Cat(models.Model):
    name = models.CharField(max_length = 30)
    count = models.IntegerField(default=0)


# for admin panel
    def __str__(self):
        return self.name 