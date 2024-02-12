from django.urls import path, include
# from .views import RegisterView, LoginView, ProfileView

app_name = "asap"

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework_category')),
    # path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    # path('profile/<int:pk>/', ProfileView.as_view()),
]