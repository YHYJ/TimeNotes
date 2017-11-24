# urls.py

```python
"""定义yj_logs的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),								# ①

    # 显示所有的题目
    url(r'^topic/$',views.topics,name='topics'),						# ②
    
    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='tipic'),		# ③
    
    # 用于添加新主题的网页
    url(r'^new_topic/$',views.new_topic,name='new_topic'),				# ④
    
    # 用于添加新文章的网页
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),	# 5

    # 用于编辑文章的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,					# 6
        name='edit_entry'),
]
```





> ①处——主页的URL模式。实际的URL模式是一个对函数url()的调用，这个函数接受三个实参：

> 第一个实参是一个正则表达式**r'^$'**
>
> > Django在urlpatterns查找与请求的URL字符串匹配的正则表达式， 表达式定义了Django可查找的模式
> >
> > > r让Python将接下来的字符串视为原始字符串
> > >
> > > 引号告诉Python正则表达式始于和终于何处
> > >
> > > 脱字符（^）让Python查看字符串的开头，美元符号让Python查看字符串的末尾
> >
> > 总体而言，这个正则表达式让Python查找开头和末尾之间没有任何东西的URL
> >
> > Python忽略不写项目的[基础URL](http://localhost:8000/)，此正则表达式与基础URL匹配，其他URL与这个正则表达式不匹配
> >
> > 如果请求的URL不与任何URL模式匹配， Django将返回一个错误页面
>
> 第二个实参指定了要调用的视图函数
>
> > 请求的URL与前述正则表达式匹配时，Django将调用views.index这个视图函数
>
> 第三个实参将这个URL模式的名称指定为index，使能够在代码的其他地方引用它
>
> > 每当需要提供到这个主页的链接时，都将使用这个名称，而不编写URL

②处——题目页面的URL模式。只是在用于主页URL的正则表达式中添加了timu/

> Django检查请求的URL时，这个模式与这样的URL匹配：
>
> > 基础URL后面跟着字符串 “timu”
> >
> > “timu” 末尾可以包含斜杠，也可以省略它，但timu后面不能有任何东西，否则就与该模式不匹配
> >
> > URL与该模式匹配的请求都将交给views.py中的函数timu()进行处理
>
> ③处——正则表达式  r'^topics/(?P<topic_id>\d+)/$'  详解
>
> > r —— 让Django将这个字符串视为原始字符串，并指出正则表达式包含在引号内
> >
> > (/(?P<topic_id>\d+)/) —— 与包含在两个斜杠内的整数匹配，并将这个整数存储在名为topic_id的实参中
> >
> > > 表达式两边的括号捕获URL中的值
> > >
> > > ?P<topic_id>将匹配的值存储到topic_id中
> > >
> > > 而表达式\d+与包含在两个斜杆内的任何数字都匹配，不管这个数字为多少位
> >
> > URL与这个模式匹配时， Django将调用视图函数topic()，并将存储在topic_id中的值作为实参传递给它
> >
> > 这个函数将使用topic_id的值来获取相应的主题
>
> ④处——这个URL模式将请求交给视图函数new_topic()
>
> 5处——这个URL模式与[URL](http://localhost:8000/new_entry/id/)匹配
>
> > 其中id是一个与主题ID匹配的数字
> >
> > 代码(?P<topic_id>\d+)捕获一个数字值，并将其存储在变量topic_id中
> >
> > 请求的URL与这个模式匹配时， Django将请求和主题ID发送给函数new_entry()
>
> 6处——在[URL](如http://localhost:8000/edit_entry/1/)中传递的ID存储在形参entry_id中
>
> > 这个URL模式将预期匹配的请求发送给视图函数edit_entry()