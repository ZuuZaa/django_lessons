from __future__ import unicode_literals
from django.db import models

# Create your models here.


class SubCat(models.Model):

    name = models.CharField(max_length = 30)
    catname = models.CharField(max_length = 30)
    catid = models.IntegerField()


# for admin panel
    def __str__(self):
        return self.name 