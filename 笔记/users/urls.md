# urls.py

```python
"""为应用程序users定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import login											# 1

from . import views

urlpatterns = [
    # 登录页面
    url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),		# 2
    
    # 注销
    url(r'^logout/$',views.logout_view,name='logout'),								# 3
    
    # 注册页面
    url(r'^register/$', views.register,name='register'),							# 4
]
```

> 1出——导入默认视图login
>
> 2处——登陆页面的URL模式与[URL](http://localhost:8000/users/login/)匹配
>
> > 这个URL中的单词users让Django在users/urls.py中查找
> >
> > 而login让它将请求发送给Django默认视图login（注意视图实参为login，而不是views.login）
> >
> > 鉴于没有编写自己的视图函数，我们传递了一个字典，告诉Django去哪里查找编写的模板
> >
> > > 这个模板包含在应用程序users而不是yj_logs中
>
> 3处——这个URL模式将请求发送给视图函数logout_view()
>
> > 这样给这个函数命名，旨在将其与将在其中调用的函数logout()区分开来
> >
> > 确保修改的是users/urls.py，而不是yj_log/ urls.py
>
> 4处——这个模式与[URL]( http://localhost:8000/users/register/)匹配，并将请求发送给编写的视图函数register()