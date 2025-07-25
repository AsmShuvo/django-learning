from django.urls import path
from .views import testView  , timeView, list_view

urlpatterns = [
    path('test/', testView, name='test'),
    path("time/", timeView, name='time'),
    path("", list_view, name='list'),
]