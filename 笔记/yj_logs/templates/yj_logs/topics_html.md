# topics.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% extends "yj_logs/base.html" %}
</head>
<body>

{% block content %}

    <p>主题</p>

    <ul>																			# ①
        {% for topic in topics %}													# ②
            <li>
                <a href="{% url 'yj_logs:topic' topic.id %}">{{ topic }}</a>		# ③
      		</li>
        {% empty %}																	# ④
            <li>尚未添加任何主题.</li>
        {% endfor %}																# ⑤
    </ul>																			# ⑥
  
  	<a href="{% url 'yj_logs:new_topic' %}">
        <button name="submit">添加新主题</button>
    </a>

{% endblock content %}
  
</body>
</html>
```

> 类似模板index.html，首先使用标签{% extends %}来继承base.html，再开始定义content块
>
> ①处——包含所有主题的项目列表的起始处
>
> > 这个网页的主体是一个项目列表，其中列出了用户输入的主题
> >
> > 在标准HTML中，项目列表被称为无序列表，用标签<ul></ul>表示
>
> ②处——使用了一个相当于for循环的模板标签，它遍历字典[context](yj_logs/views/zhuti())中的列表topics
>
> > 模板中使用的代码与Python代码存在一些重要差别：
> >
> > > Python使用缩进来指出哪些代码行是for循环的组成部分
> > >
> > > 而在模板中，每个for循环都必须使用{% endfor %}标签来显式地指出其结束位置
> > >
> > > 因此在模板中，循环类似于：
> > >
> > > ```html
> > > {% for item in list %}
> > > 	do something with each item
> > > {% endfor %}
> > > ```
>
> ③处——在循环中将每个主题转换为一个项目列表项（修改了该文件，让每个主题都链接到相应的网页）
>
> > 原为：<li>{{ topic }}</li>
> >
> > 要在模板中打印变量，需要将变量名用双花括号括起来
> >
> > 每次循环时， 代码{{ topic }}都被替换为topic的当前值
> >
> > 这些花括号不会出现在网页中，它们只是用于告诉Django使用了一个模板变量
> >
> > HTML标签<li></li>表示一个项目列表项，位于标签<li>和</li>之间的内容都是一个项目列表项
>
> ④处——使用模板标签{% empty %}告诉Django在列表topics为空时该怎么办：
>
> > 这里是打印一条消息，告诉用户还没有添加任何主题
>
> ⑤⑥处——分别结束for循环和项目列表





### 设置样式重写后





```html
{% extends "yj_logs/base.html" %}

{% block header %}																<!-- 1 -->
    <h1>所有记忆</h1>
{% endblock header %}

{% block content %}

    <ul>
    {% for topic in topics %}
        <li>
        <h3>																	<!-- 2 -->
            <a href="{% url 'yj_logs:topic' topic.id %}">{{ topic }}</a>
        </h3>
        </li>
    {% empty %}
        <li>尚未记录任何记忆</li>
    {% endfor %}
    </ul>

    <h3>
        <a href="{% url 'yj_logs:new_topic' %}">开启新记忆</a>					<!-- 3 -->
    </h3>

{% endblock content %}
```

> 1处——不需要标签{% load bootstrap3 %}，因为这个文件没有使用任何bootstrap3自定义标签
>
> 2处——为设置每个主题的样式，将它们都设置为<h3>元素，让它们在页面上显得大些
>
> 3处——对添加新主题的链接做同样的处理











