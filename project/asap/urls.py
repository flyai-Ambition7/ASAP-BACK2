from django.urls import path, include
from . import views
from .views import RegisterView, LoginView, LogoutView
app_name = "asap"
from rest_framework import routers
from asap import views
# 라우터 만들기
router = routers.DefaultRouter()
# router.register(r'tests2', views.TestViewSet2)
router.register(r'tests', views.TestViewSet)
router.register(r'posts', views.PostViewset)
router.register(r'new_menu_input', views.ItemInfoViewset)
urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    # path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    # path('profile/<int:pk>/', ProfileView.as_view()),
    path('signup', RegisterView.as_view(), name = 'signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('', include(router.urls))
]