# topic.html

> 需要显示主题的名称和条目的内容；如果当前主题不包含任何条目，需向用户指出这一点

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% extends "yj_logs/base.html" %}
</head>
<body>
  
{% block content %}

    <p>主题:{{ topic }}</p>										<!-- 1 -->

    <p>文章:</p>
  
  	<p>
        <a href="{% url 'yj_logs:new_entry' topic.id %}">
            <button name="submit">添加新文章</button>
        </a>
    </p>
  
    <ul>														  <!-- 2 -->
    {% for entry in entries %}									  <!-- 3 -->
    <li>
        <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>			  <!-- 4 -->
        <p>{{ entry.text|linebreaks }}</p>						  <!-- 5 -->
        <p>
            <a href="{% url 'yj_logs:edit_entry' entry.id %}">		<!-- 7 -->
                <button name="submit">修改文章</button>
            </a>
        </p>
    </li>
    {% empty %}													  <!-- 6 -->
    <li>
        尚未为该主题创建文章.
    </li>
    {% endfor %}
    </ul>

{% endblock content %}
  
</body>
</html>
```

> ①处——显示当前的主题
>
> > 它存储在模板变量{{ topic }}中，变量topic包含在字典context中
>
> ②处——定义一个显示每个条目的项目列表
>
> ③处——遍历条目
>
> ④处——每个项目列表项都将列出两项信息：条目的时间戳和完整的文本
>
> > 为了列出时间戳，显示属性date_added的值
> >
> > 在Django模板中，竖线（|）表示模板过滤器——对模板变量的值进行修改的函数
> >
> > 过滤器date: 'M d, Y H:i'以这样的格式显示时间戳： January 1, 2015 23:00
>
> ⑤处——显示text的完整值，而不仅仅是entry的前50个字符
>
> > 过滤器linebreaks将包含换行符的长条目转换为浏览器能够理解的格式，以免显示为一个不间断的文本块
>
> ⑥处——模板标签{% empty %}打印一条消息，告诉用户当前主题还没有条目
>
> 7处——将编辑链接放在每个条目的日期和文本后面
>
> > 在循环中使用模板标签{% url %}根据URL模式edit_entry和当前文章的ID属性 （entry.id） 来确定URL
> >
> > 链接文本为"修改文章"，它出现在页面中每个条目的后面





### 设置样式重写后



```html
{% extends "yj_logs/base.html" %}

{% block header %}																<!-- 1 -->
    <h2>{{ topic }}</h2>
{% endblock header %}

{% block content %}
    <p>
        <h4>
            <a href="{% url 'yj_logs:new_entry' topic.id %}">创作新文章</a>
        </h4>
    </p>

    {% for enrty in entries %}
        <div class="panel panel-default">										<!-- 2 -->
            <div class="panel panel-heading">									<!-- 3 -->
                <h3>															<!-- 4 -->
                    {{ enrty.date_added|date:'M d, Y H:i' }}
                    <small>														<!-- 5 -->
                        <a href="{% url 'yj_logs:edit_entry' enrty.id %}">修改文章</a>
                    </small>
                </h3>
            </div>
            <div class="panel-body">											<!-- 6 -->
                {{ entry.text|linebreaks }}
            </div>
        </div>  <!-- panel -->
    {% empty %}
        记忆角落，荒芜之地.
    {% endfor %}
    
{% endblock content %}
```

> 1处——将主题放在header块中
>
> 2、3、4、6处——创建一个面板式div元素（而不是将每个条目作为一个列表项），其中包含两个嵌套div：
>
> > 3处——一个面板标题（panel-heading） div
> >
> > > 4处——面板标题div包含条目的创建日期以及用于编辑条目的链接，它们都被设置为<h3>元素
> >
> > 6处——一个面板主体（panel-body）div
>
> 5处——对于编辑条目的链接使用标签<small>，使其比时间戳小些