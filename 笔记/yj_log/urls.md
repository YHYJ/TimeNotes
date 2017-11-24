# urls.py

```python
from django.conf.urls import url								# ①
from django.contrib import admin
from yj_logs import views										# ②

urlpatterns = [													# ③
    url(r'^admin/', admin.site.urls),							# ④
    url(r'', include('yj_logs.urls', namespace='yj_logs')),		# ⑤
    url(r'^users/',include('users.urls',namespace='users')),	# 6
]
```

> ①处——导入函数url，需要使用它来将URL映射到视图
>
> ②处——导入模块views，其中的句点让Python从当前的urls.py模块所在的文件夹中导入视图
>
> ③处——
>
> > 在这个针对整个项目的urls.py文件中，变量urlpatterns包含项目中的应用程序的URL
>
> ④处——包含模块admin.site.urls
>
> > 该模块定义了可在管理网站中请求的所有URL
>
> ⑤处——包含模块yj_logs.urls，实参namespace将yj_logs的URL同项目中的其他URL区分开
>
> 6处——包含应用程序users中的文件urls.py
>
> > 这行代码与任何以单词users打头的[URL](如http://localhost:8000/users/login/)都匹配
> >
> > 还创建了命名空间'users'，以便将应用程序yj_logs的URL同应用程序users的URL区分开来