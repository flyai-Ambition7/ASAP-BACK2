from django.shortcuts import render
from rest_framework import viewsets
from asap.models import humanInfo, Test
from asap.serializers import humanInfoSerializer, TestSerializer

# Create your views here.

class hInfoViewSet(viewsets.ModelViewSet):
    # queryset에 humanInfo 클래스에 있는 모든 정보를 담기
    queryset = humanInfo.objects.all()
    # serializer_class는 humanInfoSerializer를 이용
    serializer_class = humanInfoSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer