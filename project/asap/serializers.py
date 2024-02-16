# restFrameWork에서 사용하는 기능
# 우리가 만든 데이터 모델과 1:1 형태로(Json으로) 매칭시켜줌

from rest_framework import serializers
from .models import Img, humanInfo, Test, Version, Post, Test2, Task, User


# 시리얼라이저에 있는 모델 시리어라지어를 확장시킨 클래스
class humanInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        # 모델명은 humanInfo
        model = humanInfo
        # humanInfo에서 created를 제외한 나머지 필드만 Json 파일로 바꿔주기
        fields = ['name', 'phone_number', 'address']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('test', 'id')

#메인 테스트 용도
class TestSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Test2
        fields = ('username', 'loginID','loginPW', 'password','email', 'mobile',
                   'storeName','theme', 'purpose','resultForm',
                   'productName', 'price','info', 'time','where', 'storePhone')
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed')

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('version', )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text', 'put', 'lae')
    
class ImgSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Img
        fields = ('title', 'text', 'image')
    
#--------------------------------------------------------------
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token # Token 모델
from .models import Profile, CommonInfo, ItemInfo

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('phone',)

class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        Profile.objects.create(
            user=user,
            phone=profile_data['phone']
        )

        Token.objects.create(user=user)

        return user

from django.contrib.auth import authenticate
# Django의 기본 authenticate 함수 -> 우리가 설정한 DefaultAuthBackend인 TokenAuth 방식으로 유저를 인증해준다.
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    # write_only=True 옵션을 통해 클라이언트->서버의 역직렬화는 가능하지만, 서버->클라이언트 방향의 직렬화는 불가능하도록 해준다.
    
    def validate(self, data):
        Profile = authenticate(**data)
        if Profile:
            token = Token.objects.get(Profile=Profile) # 해당 유저의 토큰을 불러옴
            return token
        raise serializers.ValidationError( # 가입된 유저가 없을 경우
            {"error": "가입된 유저가 없습니다."}
        )
    
    # ---------------------------


class Base64ImageField(serializers.ImageField):   

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

       
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')           
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')
            
            file_name = str(uuid.uuid4())[:12] 
           
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
class ItemInfoSerializer(serializers.ModelSerializer):
    image = Base64ImageField(
        max_length=None, use_url=True, required=False
    )
    class Meta:
        model = ItemInfo
        fields = ('image','store_name', 'purpose', 'result_type', 'theme',
                  'product_name', 'price', 'description', 'business_hours', 'location', 'contact')