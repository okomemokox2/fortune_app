from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarot, name='tarot'),
    path('result/', views.tarot_result, name='tarot_result'),
    path('shuffle/', views.tarot_shuffle, name='tarot_shuffle'),
]
