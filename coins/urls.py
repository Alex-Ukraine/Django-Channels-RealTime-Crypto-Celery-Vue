from django.urls import path
from .views import index, pair_post

urlpatterns = [
    path('', index, name="home"),
    path('pair_post', pair_post, name="pair_post"),
]
