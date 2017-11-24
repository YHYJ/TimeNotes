# base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>YJLOG-1024</title>
</head>
<body>

<p>
    <a href="{% url 'yj_logs:index' %}">纪年</a> -			<!-- ① -->
    <a href="{% url 'yj_logs:topics' %}">所有主题</a> -		   <!-- ② -->
    {% if user.is_authenticated %}							  <!-- 4 -->
    	欢迎回来,{{ user.username }}						   <!-- 5 -->
  		<a href="{% url 'users:logout' %}">注销</a>			 <!-- 7 -->
    {% else %}
        <a href="{% url 'users:login' %}">登录</a>			 <!-- 6 -->
    {% endif %}
</p>

{% block content %}{% endblock content %}					  <!-- ③ -->

</body>
</html>
```

> ①处——创建一个包含项目名的段落，该段落也是一个到主页的链接
>
> > 为创建链接，使用了一个模板标签，它是用大括号和百分号（{% %}）表示的
> >
> > **模板标签**是一小段代码，生成要在网页中显示的信息
> >
> > 模板标签{% url 'learning_logs:index' %}生成一个URL，该URL与yj_log/urls.py中定义的名为index的URL模式匹配
> >
> > yj_logs是一个命名空间，而index是该命名空间中一个名称独特的URL模式
> >
> > 在简单的HTML页面中，链接是使用**锚标签**定义的：
> >
> > \<a href="link_url">link text</a>
> >
> > 让模板标签来生成URL，可让链接保持最新容易得多
> >
> > 要修改项目中的URL，只需修改urls.py中的URL模式
> >
> > 这样网页被请求时， Django将自动插入修改后的URL
> >
> > 在yj_logs项目中，每个网页都将继承base.html，因此从现在开始，每个网页都包含到主页的链接
>
> ②处——添加了一个转到显示所有主题的页面的链接——使用的也是模板标签url
>
> >在①处到主页的链接后面添加了一个连字符 - 
>
> ③处——插入了一对块标签
>
> > 这个块名为content，是一个**占位符**，其中包含的信息将**由子模板指定**
> >
> > 子模板并非必须定义父模板中的每个块
> >
> > > 因此在父模板中，可使用任意多个块来预留空间，而子模板可根据需要定义相应数量的块
>
> 4处——向已登录的用户显示一条问候语
>
> > 在Django身份验证系统中，每个模板都可使用变量user，这个变量有一个is_authenticated属性：
> >
> > > 如果用户已登录，该属性将为True，否则为False
> > >
> > > 这样能够向已通过身份验证的用户显示一条消息，而向未通过身份验证的用户显示另一条消息
>
> 5处——对已通过身份验证的用户设置属性username，使用这个属性来个性化问候语，让用户知道他已登录
>
> 6处——对于还未通过身份验证的用户显示一个到登录页面的链接
>
> 7处——注销链接放在标签{% if user.is_authenticated %}中，使得仅当用户登录后才能看到它





### 设置网页样式，删除全部代码重新编写

##### HTML文件分为两个主要部分：头部 （head）和主体 （body）

```html
{% load bootstrap3 %}															<!-- 1 -->

<!DOCTYPE html>																	<!-- 2 -->
<html lang="en"																	<!-- 3 -->
<head>																			<!-- 4 -->
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Copatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,inital-scale-1">
          
	<title>YJLOG-1024</title>													<!-- 5 -->
          
	{% bootstrap_css %}															<!-- 6 -->
	{% bootstrap_javascript %}
</head>																			<!-- 7 -->

<body>																			<!-- 8 -->

    <!-- 静态导航栏 -->
    <nav class="navbar navbar-default navbar-static-top">						<!-- 9 -->
        <div class="container">

            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed"		   <!-- 10 -->
                        data-toggle="collapse" data-target="#navbar"
                        aria-expanded="false" aria-controls="navbar">
                </button>
                <a class="navbar-brand" href="{% url 'yj_logs:index' %}">	   <!-- 11 -->
                    纪年
                </a>
            </div>

            <div id="navbar" class="navbar-collapse collapse">				   <!-- 12 -->
                <ul class="nav navbar-nav">									   <!-- 13 -->
                    <li><a href="{% url 'yj_logs:topics' %}">所有主题</a> </li>	<!-- 14 -->
                </ul>

                <ul class="nav navbar-nav navbar-right">					   <!-- 15 -->
                    {% if user.is_authenticated %}
                        <li><a>欢迎回来,{{ user.username }}</a></li>
                        <li><a href="{% url 'users:logout' %}">注销</a> </li>
                    {% else %}
                        <li><a href="{% url 'users:login' %}">登录</a> </li>
                        <li><a href="{% url 'users:register' %}">注册</a> </li>
                    {% endif %}
                </ul>														   <!-- 16 -->
            </div><!--/.nav-collapse -->

        </div>
    </nav>

    <div class="container">													   <!-- 17 -->
        
        <div class="page-header">
            {% block header %}{% endblock header %}							   <!-- 18 -->
        </div>
        <div>
            {% block content %}{% endblock content %}						   <!-- 19 -->
        </div>
        
    </div><!-- /container -->

</body>

</html>
```

> 1处——加载django-bootstrap3中的模板标签集
>
> 2处——这个文件为HTML文档
>
> 3处——声明为使用英语编写
>
> 4处——头部起始标签<head>
>
> > HTML文件的头部不包含任何内容
> >
> > 它只是将正确显示页面所需的信息告诉浏览器
>
> 5处——包含了一个title元素
>
> > 在浏览器中打开网站“YJLOG-1024”的页面时，浏览器的标题栏将显示该元素的内容
>
> 6处——使用django-bootstrap3的一个自定义模板标签
>
> > 它让Django包含所有的Bootstrap样式文件
> >
> > 接下来的标签启用可能在页面中使用的所有交互式行为，如可折叠的导航栏
>
> 7处——头部结束标签</head>
>
> 8处——主体起始标签<body>
>
> > HTML文件的主体包含用户将在页面上看到的内容
>
> 9处——一个<nav>元素，表示页面的导航链接部分
>
> > 对于这个元素内的所有内容，都将根据三个选择器（selector）：
> >
> > > navbar
> > >
> > > navbar-default
> > >
> > > navbar-static-top
> >
> > 定义的Bootstrap样式规则来设置样式。选择器决定了特定的样式规则将应用于页面上的哪些元素
>
> 10处——这个模板定义了一个按钮，它将在浏览器窗口太窄、无法水平显示整个导航栏时显示出来
>
> > 如果用户单击这个按钮，将出现一个下拉列表，其中包含所有的导航元素
> >
> > 在用户缩小浏览器窗口或在屏幕较小的移动设备上显示网站时， collapse会使导航栏折叠起来
>
> 11处——在导航栏的最左边显示项目名，并设置其为到主页的链接，因为它将出现在这个项目的每个页面中
>
> 12、13、14处——定义了一组让用户能够在网站中导航的链接
>
> > 13处——导航栏其实就是一个以<ul>打头的列表
> >
> > 14处——其中每个链接都是一个列表项（<li>）
> >
> > 要在导航栏中添加更多的链接，可插入更多下述结构的行：
> >
> > > <li>\<a href="{% url 'learning_logs:title' %}">Title</a></li>
>
> 15处——添加了第二个导航链接列表，这里使用的选择器为navbar-right
>
> > navbar-right设置一组链接的样式，使其出现在导航栏右边——登录链接和注册链接通常出现在这里
> >
> > 要么显示问候语和注销链接，要么显示登录和注册链接
>
> 16处——结束包含导航栏的元素
>
> 17、18、19处——<div>起始标签，其class属性为container
>
> > div是网页的一部分，可用于任何目的，并可通过：
> >
> > > 边框
> > >
> > > 元素周围的空间（外边距）
> > >
> > > 内容和边框之间的间距（内边距）
> > >
> > > 背景色
> > >
> > > 和其他样式规则
> >
> > 来设置其样式
> >
> > 这个div是一个容器，其中包含两个元素：
> >
> > > 18处——一个新增的名为header的块
> > >
> > > > header块的内容告诉用户页面包含哪些信息以及用户可在页面上执行哪些操作
> > > >
> > > > 其class属性值page-header将一系列样式应用于这个块
> > >
> > > 19处——一个新增的名为content的块
> > >
> > > > content块是一个独立的div，未使用class属性指定样式