from django.urls import path

from . import apis

urlpatterns = [
    path('auth-token/', apis.AuthTokenView.as_view()),
    path('profile/', apis.ProfileView.as_view()),
]
