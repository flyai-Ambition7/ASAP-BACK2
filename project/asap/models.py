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