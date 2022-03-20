from django.urls import path

from YCU_Supervisory_System.user import views

urlpatterns = [
    path('login', views.Login.as_view()),
    path('register', views.Register.as_view())
]