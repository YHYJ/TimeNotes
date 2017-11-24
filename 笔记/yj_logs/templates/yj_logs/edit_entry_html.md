# edit_entry.html

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
        <a href="{% url 'yj_logs:topic' topic.id %}">{{ topic }}</a>
    </p>

    <p>修改文章：</p>

    <form action="{% url 'yj_logs:edit_entry' entry.id %}" method="post">		# 1
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">提交修改</button>									  # 2
    </form>

{% endblock content %}

</body>
</html>
```

> 1处——实参action将表单发回给函数edit_entry()进行处理
>
> > 标签{% url %}中，将文章ID作为一个实参，让视图对象能够修改正确的文章对象
>
> 2处——将提交按钮命名为‘提交修改’，以提醒用户：单击该按钮将保存所做的编辑，而不是创建一个新文章