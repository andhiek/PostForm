from django.urls import re_path, include


from . import views

app_name = 'contact'
urlpatterns = [
    re_path(r'^create/$', views.create, name='create'),
    re_path(r'^$', views.index, name='index'),
]
