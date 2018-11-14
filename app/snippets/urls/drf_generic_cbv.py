from django.urls import path
from ..views import drf_generic_cbv as views
urlpatterns = [
    path('snippets/', views.SnippetList),
    path('snippets/<int:pk>', views.SnippetDetail),
]