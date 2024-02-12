# Create your views here.
# REST Framework는 ViewSets라는 추상클래스를 제공한다. 이 녀석을 통해 개발자는 API의 상호작용이나 상태별 모델에 집중할 시 있다. view과 유사한 형태이다. 단 GET PUT이 아닌 READ UPDATE 메서드를 지원한다.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from rest_framework import generics, status

from asap.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer

from rest_framework.response import Response
from .permissions import CustomReadOnly

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) #예외처리
        token = serializer.validated_data # validate()의 리턴값인 token을 받아온다.
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    
   
    
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [CustomReadOnly]
