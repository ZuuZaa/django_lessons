from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Main)
admin.site.register(RelatedPerson)
admin.site.register(Note)
admin.site.register(Customer)

