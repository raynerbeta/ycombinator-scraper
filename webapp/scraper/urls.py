from django.urls import path
from .views import entries_view

urlpatterns = [
    path("", entries_view, name="entries"),
]
