from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
# GET : 누구나 / PUT,PATCH : 해당 유저만

    def has_object_permission(self, request, view, obj): #해당객체 오브젝트
        if request.method in permissions.SAFE_METHODS: # 안전한 메소드(GET)면
            return True
        return obj.user == request.user
    
    #커스텀 권한 만들기

    #커스텀 권한 클래스는 permissions.BasePermission을 상속받아와서 작성한다.

# 조회, 수정 시에 모두 프로필 전체에 대한 요청은 없고 각 객체에 대한 요청만 있으므로 has_object_permission 메소드를 가져와서 작성해준다.

# permissions.SAFE_METHODS는 데이터에 영향을 미치지 않는 메소드를 의미한다. 이런 요청은 True로 반환하여 통과시키고, PUT/PATCH 등의 요청에는 요청으로 들어온 user와 객체의 user를 비교해서 같으면 True를 반환하여 통과시켜준다.