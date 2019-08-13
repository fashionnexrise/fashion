from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('mens/', views.mens, name='mens'),
    path('login/', LoginView.as_view(template_name='myblog/login.html'), name="login"),
]

