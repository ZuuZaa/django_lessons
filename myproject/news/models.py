from __future__ import unicode_literals
from django.db import models

# Create your models here.


class News(models.Model):
    name = models.CharField(max_length = 30)
    category = models.CharField(max_length = 30, default = '-')
    catid = models.IntegerField(default = 0)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(default = '-', max_length = 12)
    picname = models.CharField(max_length = 100, default = '-')
    picurl = models.CharField(max_length = 130, default = '-')
    writer = models.CharField(max_length = 30)
    view = models.IntegerField(default = 0)

# for admin panel
    def __str__(self):
        return self.name + " | " + str(self.pk)
