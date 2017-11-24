# register.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% extends "yj_logs/base.html" %}
</head>
<body>

{% block content %}

    <form method="post" action="{% url 'users:register' %}">
        {% csrf_token %}
        {{ form.as_p }}																# 1

        <button name="submit">注册新用户</button>
        <input type="hidden" name="next" value="{% url 'yj_logs:index' %}" />
    </form>

{% endblock content %}

</body>
</html>
```

> 1处——使用方法as_p让Django在表单中正确地显示所有的字段
>
> > 包括错误消息——如果用户没有正确地填写表单