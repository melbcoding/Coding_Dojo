from django.urls import path
from . import views

urlpatterns = [
path('', views.index),
path('register', views.register),
path('login', views.login),
path('logoff', views.logoff),
path('dashboard', views.dashboard),
path('create', views.create),
path('delete', views.delete)
]
