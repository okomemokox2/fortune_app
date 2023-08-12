from django.urls import path
from . import views

app_name = 'accounts'  # 名前空間を設定

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]
