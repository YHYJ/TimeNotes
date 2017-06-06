from django.contrib import admin

# Register your models here.——注册模型

from yj_logs.models import Topic,Entry

admin.site.register(Topic)
admin.site.register(Entry)
