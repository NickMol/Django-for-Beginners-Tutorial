from django.urls import path, include
from users import views as views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('users/signup',views.signup,name='signup'),
    path('users/login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login')
]
