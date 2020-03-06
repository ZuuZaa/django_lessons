from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Main(models.Model):
    name = models.CharField(max_length = 30)
    about = models.TextField(default = '-')
    fb = models.CharField(default = '-', max_length = 30)
    tw = models.CharField(default = '-', max_length = 30)
    yt = models.CharField(default = '-', max_length = 30)

# for admin panel
    def __str__(self):
        return self.name + " | " + str(self.pk)


from django.db import models

# Create your models here.

class RelatedPerson(models.Model):

    first_name = models.CharField( max_length=50 )
    last_name = models.CharField( max_length=50 )
    fathers_name = models.CharField( max_length=50 )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Note(models.Model):

    name = models.CharField( max_length=50 )

    def __str__(self):
        return self.name


class Customer(models.Model):

    first_name = models.CharField( max_length=50 )
    last_name = models.CharField( max_length=50 )
    fathers_name = models.CharField( max_length=50 )

    related_person = models.ForeignKey(RelatedPerson, on_delete=models.CASCADE, null=True, blank=True)

    phone_number_1 = models.CharField( max_length=50 )
    phone_number_2 = models.CharField( max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=150)


    class Sources(models.TextChoices):
        FaceBook = '1', "Facebook"
        Instagram = '2', "Instagram"
        Google = '3', "Google"
        acquainted = '4', "Tanış məsləhəti"

    source = models.CharField(
        max_length=2,
        choices=Sources.choices,
        default=Sources.acquainted,
    )

    note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True)

    class Statuses(models.TextChoices):
        next = '5', "Növbəti"
        cancel = '6', "İmtina et"
        delay = '7', "Təxirə sal"

    status = models.CharField(
        max_length=2,
        choices=Statuses.choices,
        default=Statuses.next,
    )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    