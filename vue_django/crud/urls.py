from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('save', views.save, name="save"),
    path('update', views.update, name="update"),
    path('delete', views.delete, name="delete"),
]
