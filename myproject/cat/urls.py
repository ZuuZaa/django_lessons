from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^panel/cat/list$', views.cat_list, name = 'cat_list'),
    url(r'^panel/cat/add$', views.cat_add, name = 'cat_add'),

]