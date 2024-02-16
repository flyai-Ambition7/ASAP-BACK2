from django.contrib import admin

# Register your models here.
from asap.models import Task, humanInfo, Test, Test2
from asap.models import CommonInfo, ItemInfo
admin.site.register(humanInfo)
admin.site.register(Test)
admin.site.register(Test2)
admin.site.register(Task)

admin.site.register(CommonInfo)
admin.site.register(ItemInfo)