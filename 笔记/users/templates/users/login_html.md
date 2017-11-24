# login.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% extends "yj_logs/base.html" %}
</head>
<body>

{% block content %}

    {% if form.errors %}														# 1
    <p>用户名或密码错误，请重试</p>
    {% endif %}

    <form method="post" action="{% url 'users:login' %}">						# 2
    {% csrf_token %}
    {{ form.as_p }}																# 3

    <button name="submit">登录</button>										   # 4
    <input type="hidden" name="next" value="{% url 'yj_logs:index' %}" />		# 5
    </form>

{% endblock content %}

</body>
</html>
```

> 该模板也继承base.html，旨在确保登录页面的外观与网站的其他页面相同
>
> > 一个应用程序中的模板可继承另一个应用程序中的模板
>
> 1处——如果表单的errors属性被设置
>
> > 显示一条错误消息，指出输入的用户名—密码对与数据库中存储的任何用户名—密码对都不匹配
>
> 2处——要让登录视图处理表单，因此将实参action设置为登录页面的URL
>
> 3处——登录视图将一个表单发送给模板，在模板中显示这个表单
>
> 4处——添加一个登录按钮
>
> 5处——包含了一个隐藏的表单元素——'next'
>
> > 实参value告诉Django在用户成功登录后将其重定向到什么地方——在这里是主页





### 设置样式重写后

```html
{% extends "yj_logs/base.html" %}
{% load bootstrap3 %}															<!-- 1 -->

{% block header %}																<!-- 2 -->
    <h2>登录笔记</h2>
{% endblock header %}

{% block content %}

    <form method="post" action="{% url 'users:login' %}" class="form">			<!-- 3 -->
        {% csrf_token %}
        {% bootstrap_form form %}												<!-- 4 -->

        {% buttons %}															<!-- 5 -->
        <button name="submit" class="bth bth-primary">登录</button>
        {% endbuttons %}

        <input type="hidden" name="next" value="{% url 'yj_logs:index' %}"/>
    </form>

{% endblock content %}

```

> 1处——在这个模板中加载bootstrap3模板标签
>
> 2处——定义了header块
>
> > 它描述了这个页面是做什么用的
> >
> > 注意，从这个模板中删除了{% if form.errors %}代码块，因为django-bootstrap3会自动管理表单错误
>
> 3处——添加了属性class="form"
>
> 4处——使用模板标签{% bootstrap_form %}来显示表单 
>
> > 这个标签替换了以前的标签{{ form.as_p }}
> >
> > 模板标签{%booststrap_form %}将Bootstrap样式规则应用于各个表单元素
>
> 5处——bootstrap3起始模板标签{%buttons %}将Bootstrap样式应用于按钮