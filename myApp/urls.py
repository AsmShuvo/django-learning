from django.urls import path
from .views import testView  , timeView, list_view, detail_view, update_view, delete_view

urlpatterns = [
    path('test/', testView, name='test'),
    path("time/", timeView, name='time'),
    path("", list_view, name='list'),
    path("<id>", detail_view, name='detail'),
    path("<id>/update", update_view, name='update'),
    path("<id>/delete", delete_view, name='delete'),
]