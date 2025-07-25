from django.urls import path
from .views import testView  , timeView

urlpatterns = [
    path('test/', testView, name='test'),
    path("time/", timeView, name='time'),
]