from django.urls import path
from .views import RaceListView

urlpatterns = [
    path('', RaceListView.as_view()),
]