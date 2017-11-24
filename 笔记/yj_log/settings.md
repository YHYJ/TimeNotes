# settings.py

### 将应用程序包含到项目

> 要使用模型，必须让Django将应用程序包含到项目中
>
> settings.py（在yj_log文件夹中）的INSTALLED_APPS列表告诉Django哪些应用程序安装在项目中：

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 第三方应用程序
	'bootstrap3',							# 1
    
    # 我的应用程序
    'yj_logs',
    'users',
]


...
# settings.py的最后
...


# 我的设置——未登录用户查看主题页面重定向到登陆页面
LOGIN_URL = '/users/login/'

# django-bootstrap3的设置								# 2
BOOTSTRAP3 = {
    'include_jquery': True,
}

# Heroku设置
if os.getcwd() == '/app':														# 3
    import dj_database_url														# 4
    DATABASES = {
        'default':dj_database_url.config(default='postgres://localhost')
    }
    
    # 让request.is_secure()承认X-Forwarded-Proto头
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')				# 5
    
    # 支持所有的主机头 (host heaser)
    ALLOWED_HOSTS = ['*']														# 6
    
    # 静态资产配置
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))						# 7
    STATIC_ROOT = 'staticfiles'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR,'static'),
    )
```

> 通过将应用程序编组，在项目不断增大，包含更多的应用程序时，有助于对应用程序进行跟踪
>
> 1处——添加'bootstrap3'
>
> > 新建一个用于指定其他开发人员开发的应用程序的片段，将其命名为“第三方应用程序”，
> >
> > 并在其中添加'bootstrap3'
>
> 2处——使用该设置就无需手工下载jQuery并将其放到正确的地方
>
> 3处——使用函数getcwd()，它获取当前的工作目录（当前运行的文件所在的目录）
>
> > 在Heroku部署中，这个目录总是/app
> >
> > 在本地部署中，这个目录通常是项目文件夹的名称（就该项目而言为yj_log）
> >
> > 这个if测试确保仅当项目被部署到Heroku时，才运行这个代码块
> >
> > 这种结构能够将同一个设置文件用于本地开发环境和在线服务器
>
> 4处——导入dj_database_url，用于在Heroku上配置服务器
>
> > Heroku使用PostgreSQL（也叫Postgres）——一种比SQLite更高级的数据库
> >
> > 这些设置对项目进行配置，使其在Heroku上使用Postgres数据库
>
> 5处——支持HTTPS请求
>
> 6处——让Django能够使用Heroku的URL来提供项目提供的服务
>
> 7处——设置项目，使其能够在Heroku上正确地提供静态文件

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 让Django在根模板目录中查找错误页面模板
        'DIRS': [os.path.join(BASE_DIR,'yj_log/templates')],		
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



---

### 使Django支持中文

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
```

**改为**

```python
#将英文改为中文
LANGUAGE_CODE = 'zh-hans'

#把国际时区改为中国时区
TIME_ZONE = 'Asia/Shanghai'
```

---

###未登录用户查看主题重定向到登陆页面，在最后添加：

```python
LOGIN_URL = '/users/login/'
```

