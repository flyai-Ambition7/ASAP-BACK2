from django.contrib import admin

# Register your models here.
from asap.models import humanInfo, Test
admin.site.register(humanInfo)
admin.site.register(Test)