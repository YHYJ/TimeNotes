# views.py

```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.——创建users的视图函数

def logout_view(request):
    """注销账户"""
    logout(request)												# 1
    return HttpResponseRedirect(reverse('yj_logs:index'))		# 2

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空注册表单
        form = UserCreationForm()													# 1
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)									# 2

        if form.is_valid():															# 3
            new_user = form.save()													# 4
            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username,			# 5
                                              password=request.POST['password1'])
            login(request,authenticated_user)										# 6
            return HttpResponseRedirect(reverse('yj_logs:index'))					# 7
    context = {'form':form}
    return render(request,'users/register.html',context)
```

导入部分：

> 从django.contrib.auth中导入函数login()，logout()和authenticate()
>
> > logout()和authenticate()在用户正确地填写了注册信息时让其自动登录
>
> 还导入了默认表单UserCreationForm

logout_view()函数：

> 1处——调用函数logout()，它要求将request对象作为实参
>
> 2处——注销后重定向到主页

register()函数：

> 1处——响应的不是POST请求就创建一个UserCreationForm实例，且不给它提供任何初始数据
>
> 2处——响应的是POST请求就根据提交的数据创建一个UserCreationForm实例
>
> 3处——检查这些数据是否有效：
>
> > 就这里而言，有效是指用户名未包含非法字符，输入的两个密码相同，以及用户没有试图做恶意的事情
>
> 4处——提交的数据有效就调用表单的方法save()，将用户名和密码的散列值保存到数据库中
>
> > 方法save()返回新创建的用户对象，这里将其存储在new_user中
>
> 5处——调用authenticate()，并将实参new_user.username和possword传递给它
>
> > 用户注册时，被要求输入密码两次
> >
> > 由于表单是有效的，可知输入的这两个密码是相同的，因此可以使用其中任何一个
> >
> > 这里从表单的POST数据中获取与键'password1'相关联的值
> >
> > 如果用户名和密码无误：
> >
> > > 方法authenticate()返回一个通过了身份验证的用户对象，将其存储在authenticated_user中
>
> 6处——调用函数login()，并将对象request和authenticated_user传递给它，这将为新用户创建有效的会话
>
> 7处——将用户重定向到主页，其页眉中显示了一条个性化的问候语，让用户知道注册成功了