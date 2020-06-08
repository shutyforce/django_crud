from django.urls import path
from . views import signup
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('signup/', signup, name='signup'),
  path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]