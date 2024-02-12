from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # primary_key를 User의 pk로 설정하여 통합적으로 관리
    name = models.CharField(max_length=50)
    call_num = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile/', default='default.png')

@receiver(post_save, sender=User) # 유저모델하고 프로필 연결
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# 1:1 Model은 기본 User 모델에 1대1로 연결되는 새로운 모델을 하나 만들어 주는 방법이다. DB의 1대1 관계 개념을 활용하는 것으로 User 모델을 직접 건들지 않으면서 필드를 추가할 수 있는 방법이다. 여기서는 이 방법을 채택하여 사용해줄 예정이다.
# 좋은 방법이긴 하지만 두 개의 모델을 연결하여 사용하기 때문에 모델 1개를 사용하는 것보다 느릴 수밖에 없다. 어렵진 않지만 효율적인 방법도 아니긴 하다.
# from django.contrib.auth.models import AbstractUser
# from datetime import date

# class Duser(AbstractUser):
#     sex = models.CharField(max_length=20, null=True)
#     b_type = models.CharField(max_length=30, null=True)
#     height = models.IntegerField(blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#     birth = models.DateField(blank=True, null=True)