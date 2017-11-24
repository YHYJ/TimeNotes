# new_entry,html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% extends 'yj_logs/base.html' %}
</head>
<body>

{% block content %}

    <p>
        <a href="{% url 'yj_logs:topic' topic.id %}">{{ topic }}</a>			# 1
    </p>

    <p>添加新文章：</p>

    <form action="{% url 'yj_logs:new_entry' topic.id %}" method="post">		# 2
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">完成</button>
    </form>

{% endblock content%}

</body>
</html>
```

> 1处——在页面顶端显示主题，让用户知道他是在哪个主题中添加文章
>
> > 该主题名也是一个链接，可用于返回到该主题的主页面
>
> 2处——单的实参action包含URL中的topic_id值，让视图函数能够将新文章关联到正确的主题
>
> > 除此之外，这个模板与模板new_topic.html完全相同