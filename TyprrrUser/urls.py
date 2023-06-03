from django.urls import path
from .views import BlackListTokenView, UserCreateView, UserListView, UserDetailView, UserProfileView

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('register/', UserCreateView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('login/', BlackListTokenView.as_view()),
]