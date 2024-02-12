# from django.urls import path
# from . import views
# # from .views import (Questions_view, dis_information_view, RecordView, UserDetailView)

# app_name = "asap"

# urlpatterns = [
#     # path('login/', views.Login, name="login"), # 로그인 URL
#     # path('logout/', views.Logout, name="logout"), # 로그아웃
#     # path('signup/', views.Signup, name="signup"), # 회원가입 URL
#     # path('home', views.home, name='home'),
    
#     # path('read_sensor/', views.read_sensor, name='read_sensor'),
#     # path('send_command/', views.send_command, name='send_command'),
#     # path('record/', RecordView.as_view(), name='record'),
#     # path('dis_information/', dis_information_view, name='dis_information'),
#     # path('inform/', UserDetailView.as_view(), name='inform'),
#     # path('questions/', Questions_view, name='questions'),
# ]

 

# app/urls.py
from django.urls import path
from .views import RegisterView, LoginView, ProfileView

app_name = "asap"

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
]