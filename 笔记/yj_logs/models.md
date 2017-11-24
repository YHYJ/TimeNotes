# models.py

## '/yj_logs/models/'

```python
from django.db import models
from django.contrib.auth.models import User							# 1

# Create your models here.——定义模型。模型即类,类即数据库表

class Topic(models.Model):
    """主题"""
    text = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User)									# 2

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = '主题'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """关于某个主题的具体信息"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:30] + "..."
```

> 1处——导入django.contrib.auth中的模型User
>
> 2处——在Topic中添加字段owner，它建立到模型User的外键关系









---

## 其他

> 在数据库里创建一个名为 **Topic** 的表格，这个表格的列名为 **text**和**date_added**，Django 会自动创建列 id
>
> 从 Python 代码翻译成数据库语言时其规则是
>
> > 一个 Python 类对应一个数据库表格，类名即表名
> >
> > 类的属性对应着表格的列，属性名即列名

```python
from django.db import models        
from django.contrib.auth.models import User

# Create your models here——模型即类,类即数据库表

class Category(models.Model):	# Django 要求模型必须继承 models.Model 类
    """创建 分类-Category 数据库表"""
    name = models.CharField(max_length=100)	   			# ①
    #date = models.DateTimeField(auto_now_add=True)		# ②
    
    def __str__(self):									# ③
        """返回模型的简单信息"""
        return self.text
```

>①处——为新建主题命名
>
>> CharField 指定了分类名 name 是字符型
>>
>> CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库
>
>②处——DateTimeField，记录日期和时间的数据
>
>>实参auto_add_now=True——每当用户创建新主题时让Django将这个属性自动设置成当前的日期和时间
>
>③处——\_\_str\_\_()方法
>
>> Django调用方法\_\_str\_\_()使用默认属性来显示有关主题的简单信息

```python
class Tag(models.Model):
    """创建 标签-Tag 数据库表"""
    name = models.CharField(max_length=100)
    #date = models.DateTimeField(auto_now_add=True)
```

> 一定要继承 models.Model 类

```python
class Post(models.Model):
    """创建 文章-Post 数据库表"""

    title = models.CharField(max_length=70)						# ①

    body = models.TextField()									# ②

    created_time = models.DateTimeField()						# ③
    modified_time = models.DateTimeField()						# ④

    excerpt = models.CharField(max_length=200, blank=True)		# ⑤

    category = models.ForeignKey(Category)						# ⑥
    tags = models.ManyToManyField(Tag, blank=True)				# ⑦

    author = models.ForeignKey(User)							# ⑧
```

> ①处——文章标题
>
> >限制字符长度70
>
> ②处——文章正文
>
> > CharField 存储比较短的字符串
> >
> > 文章的正文可能是一大段文本，因此使用 TextField 来存储大段文本
>
> ③④处——文章的创建时间和最后一次修改时间
>
> >这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型
>
> ⑤处——文章摘要
>
> > 可以没有文章摘要，但默认情况下 CharField 要求必须存入数据，否则就会报错，指定 CharField 的 blank=True 参数值后就可以允许空值
>
> ⑥⑦处——创建Category和Tag类的实例，并把文章对应的数据库表和分类、标签对应的数据库表关联起来
>
> > ⑥——
> >
> > > 一篇文章只对应一个分类，但一个分类下可以有多篇文章，所以使用 ForeignKey，即一对多的关联关系
> >
> > ⑦——
> >
> > > 一篇文章可有多个标签，同一个标签下也可有多篇文章，所以使用 ManyToManyField，即多对多的关联关系
> > >
> > > 规定文章可以没有标签，因此为标签 tags 指定了 blank=True
>
> ⑧处——文章作者
>
> >User 是从 django.contrib.auth.models 导入的
> >
> >> django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 已经写好的用户模型
> >
> >通过 ForeignKey 把文章和 User 关联起来



