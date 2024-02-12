from django.contrib import admin

# Register your models here.

# 관리자 페이지에서 이렇게도 설정할 수 있구나 그래서 이 파일이 있는거고..
#Profile 모델을 admin에 등록하면 관리자 페이지에서 확인은 가능하지만, User 과 따로 떨어져 있다 보니 불편해진다.

# User와 Profile 두 모델이 같은 모델인 것처럼 함께 보기 위해 admin.py에 다음과 같이 작성해주도록 하자.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile" # 복수형으로 이름 표기하지 않도록 직접 지정
    
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#이렇게 하면 유저에 프로필 모델 만들었던 것도 같이 보여준다.