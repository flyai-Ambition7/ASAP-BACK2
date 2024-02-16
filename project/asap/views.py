from django.shortcuts import render
from rest_framework import viewsets
from asap.models import humanInfo, Test, Version, Post, Test2, Task
from asap.serializers import TestSerializer2, PostSerializer, humanInfoSerializer, TestSerializer, VersionSerializer, TaskSerializer
from rest_framework import generics
# Create your views here.

class hInfoViewSet(viewsets.ModelViewSet):
    # queryset에 humanInfo 클래스에 있는 모든 정보를 담기
    queryset = humanInfo.objects.all()
    # serializer_class는 humanInfoSerializer를 이용
    serializer_class = humanInfoSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TestViewSet2(viewsets.ModelViewSet):
    queryset = Test2.objects.all()
    serializer_class = TestSerializer2

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


#----------------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, ItemInfoSerializer
from .models import Profile, ItemInfo
from rest_framework import generics, status
from django.utils import timezone
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) #예외처리
        token = serializer.validated_data # validate()의 리턴값인 token을 받아온다.
        return Response({"token": token.key}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        
        # 클라이언트에서 JWT 토큰 제거 위해 쿠기 삭제
        response.delete_cookie('jwt')
        response.data = {
            'message' : 'success' # 응답 메시지
        }
        return response
    
class ItemInfoViewset(viewsets.ModelViewSet):
    queryset = ItemInfo.objects.all()
    serializer_class = ItemInfoSerializer

# blank - 필수 입력여부, null - null값 허용?아마?
 # Event_Inpu, Opening_Input - 아직 입력값 정해지지 않음.
# class Event_Inpu(models.Model):
# class Opening_Input(models.Model):

# class Gpt_Prompt(models.Model):
#     summary = models.CharField(max_length=100) # gpt가 요약해주는 글

# # 현성이 fs.chunks로 되어있음. ai에서 자동 생성해주는 table -> document
# # 자동으로 생성해줘서 fs.chunks로 되있어서 _로 바꿔줘야 함.
# class fs_chunks(models.Model): # ai에서 자동 생성해주는 table -> document
#     Gpt_Prompt_id = models.ForeignKey(Gpt_Prompt)
#     data = models.ImageField(upload_to='asap', null=True)
#     BinaryField
#     create_date = models.DateTimeField(auto_now_add=True) # 생성날짜