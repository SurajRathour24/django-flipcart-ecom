from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.user_registeration, name="signup"),
    path('signin/', views.user_signin, name="signin"),
    path('profile/', views.user_profile, name="profile"),
    path('signout', views.user_logout, name="signout"),
    path('changepass', views.change_password, name="changepass"),
]
