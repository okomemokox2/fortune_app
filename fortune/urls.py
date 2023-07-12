from django.urls import path
from . import views

urlpatterns = [
    path('birth/', views.fortune_telling, name='fortune_telling'),
    path('int/', views.fortune_telling_int, name='fortune_telling_int'),
]
