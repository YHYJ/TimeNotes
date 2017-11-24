# new_topic.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% extends 'yj_logs/base.html' %}
</head>
<body>

{% block content %}

    <p>添加新主题：</p>

    <form action="{% url 'yj_logs:new_topic' %}" method="post">			# ①
        {% csrf_token %}												# ②
        {{ form.as_p }}													# ③
        <button name="submit">提交</button>							  # ④
    </form>

{% endblock content %}

</body>
</html>
```

> ①处——定义了一个HTML表单
>
> > 实参action告诉服务器将提交的表单数据发回给视图函数new_topic()
> >
> > 实参method让浏览器以POST请求的方式提交数据
>
> ②处——Django使用模板标签{% csrf_token %}来防止攻击者利用表单来获得对服务器未经授权的访问
>
> > 这种攻击被称为跨站请求伪造
>
> ③处——显示表单，从中可知Django使得完成显示表单等任务有多简单：
>
> > 只需包含模板变量{{ form.as_p }}，就可让Django自动创建显示表单所需的全部字段
> >
> > 修饰符as_p让Django以段落格式渲染所有表单元素，这是一种整洁地显示表单的简单方式
>
> ④处——定义一个提交按钮





### 设置样式重写后





```html
{% extends 'yj_logs/base.html' %}
{% load bootstrap3 %}

{% block header %}																<!-- 1 -->
    <h2>开启新主题:</h2>
{% endblock header %}


{% block content %}

    <form action="{% url 'yj_logs:new_topic' %}" method="post" class="form">	<!-- 2 -->
        {% csrf_token %}
        {% bootstrap_form form %}												<!-- 3 -->

    {% buttons %}																<!-- 4 -->
        <button name="submint" class="bth bth-primary">完成</button>
    {% endbuttons %}

    </form>

{% endblock content %}

```

> 1处——加载bootstrap3，添加header块并在其中包含合适的消息
>
> 2处——在标签<form>中添加属性class="form"
>
> 3处——使用模板标签{% bootstrap_form %}代替{{ form.as_p }}
>
> 4处——使用bootstrap3结构来定义提交按钮