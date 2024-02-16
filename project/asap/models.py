from django.db import models

# Create your models here.
class humanInfo(models.Model) :
    # 이름
    name = models.CharField(max_length=10)
    # 핸드폰 번호
    phone_number = models.CharField(max_length=13)
    # 주소(길이 제한 없음)
    address = models.TextField()
    # 데이터 생성 날짜(현재시간기준 자동 저장)
    created = models.DateTimeField(auto_now_add=True)

    # created 기준 오름차순 정렬
    class Meta :ordering = ['created']

class Test(models.Model):
    test = models.CharField(max_length=100)

    def __str__(self):
        return self.test

#테스트완료 
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    put = models.TextField()
    lae = models.CharField(max_length = 100)

class Version(models.Model):
    version = models.CharField(max_length=10)

    def __str__(self):
        return self.version
class Test2(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    storeName = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    resultForm = models.CharField(max_length=200)
    productName = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    where = models.CharField(max_length=200)
    storePhone = models.CharField(max_length=200)
    loginID = models.CharField(max_length=200)
    loginPW = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Img(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="%Y/%m/%d")

# ---------------------------
from datetime import date
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # primary_key를 User의 pk로 설정하여 통합적으로 관리
    phone = models.CharField(max_length=50)

# 공통 입력사항
class CommonInfo(models.Model):
    image = models.ImageField(null = True, blank = True,)
    store_name = models.CharField(max_length=50, blank=False) # 가게명
    purpose = models.CharField(max_length=50, blank=False) # 사용 목적
    result_type = models.CharField(max_length=10, blank=False) # 결과물 형태 (배너입력)
    theme = models.CharField(max_length=50, blank=False) #결과물 테마

# 상품을 홍보하는 경우    
class ItemInfo(CommonInfo, models.Model):
    product_name = models.CharField(max_length=50, blank=False) # 상품명
    price =  models.IntegerField() # 상품 가격
    description = models.TextField() # 상품 설명
    business_hours = models.CharField(max_length=30, blank=True) # 가게 영업시간
    location = models.CharField(max_length=100, blank= True) # 가게 위치
    contact = models.CharField(max_length=20, blank= True) # 가게 전화번호



class Chunk(models.Model):
    image_data = models.ImageField(upload_to='chunks/')
    encoded_image_data = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Chunk {self.id}'