# index.html

```html
<p>Log-1024</p>p>					

<p>随心记录生命点滴.</p>p>
```

> 标签<p></p>标识段落；标签<p>指出了段落的开头位置，标签</p>指出了段落的结束位置
>
> 定义了两个段落：第一个充当标题，第二个阐述了用户可使用“YJ的Log”来做什么。

### 继承父模板重写后：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% extends "yj_logs/base.html" %}			# ①
</head>
<body>

{% block content %}								# ②

    <p>我什么也没忘，但有些事只适合收藏.</p>

{% endblock content %}							# ③

</body>
</html>
```

>①处——将标题Log-1024替换成了从父模板那里继承的代码
>
>> 子模板的第一行必须包含标签{% extends %}，让Django知道它继承了哪个父模板
>>
>> 文件base.html位于文件夹yj_logs中，因此父模板路径中包含yj_logs
>>
>> ①处导入模板base.html的所有内容，让index.html能够指定要在content块预留的空间中添加的内容
>
>②处——插入了一个名为content的{% block %}标签，以定义content块
>
>> 不是从父模板继承的内容都包含在content块中，在这里是一个描述项目“yj_logs”的段落
>
>③处——标签{% endblock content %}指出了内容定义的结束位置





### 设置样式重写后

```html
{% extends "yj_logs/base.html" %}

{% block header %}														<!-- 1 -->
    <div class="jumbotron">												<!-- 2 -->
        <h3>我什么也没忘，但有些事只适合收藏.</h3>
    </div>
{% endblock header %}

{% block content %}
    <h3>																<!-- 3 -->
        <a href="{% url 'users:register' %}">注册账号</a>
        —— 记录流淌于记忆中想忘难忘的事
    </h3>
    <h1>


    </h1>
    <h1>
        和世界交手的这许多年，你是否光彩依旧，兴致盎然.
    </h1>
{% endblock content %}
```

> 1处——定义header块包含的内容
>
> 2处——在一个jumbotron元素中放置一条简短的标语——我什么也没忘，但有些事只适合收藏.
>
> > 让首次访问者大致知道“时光笔记”是做什么用的
>
> 3处——通过添加一些文本，做了更详细的说明
>
> > 邀请用户建立账户，并描述了用户可执行的两种主要操作：添加新主题以及在主题中创建文章