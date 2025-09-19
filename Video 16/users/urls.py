from django.urls import path, include
from users import views as views

urlpatterns = [
    path('users/signup',views.signup,name='signup')
]
