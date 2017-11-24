# views.py

```python
from django.shortcuts import render		#函数render()根据视图函数提供的数据渲染响应
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required	# 6

from .models import Topic,Entry							     # ①
from .forms import TopicForm,EntryForm

# Create your views here.——在此创建视图函数

def index(request):						#主页视图函数
    """yj_logs的主页"""
    return render(request,'yj_logs/index.html')

@login_required												# 7
def topics(request):										  # ②
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')		# ③ 8
    context = {'topics':topics}								  # ④
    return render(request,'yj_logs/topics.html',context)	  # ⑤
```

> URL请求与刚才定义的模式匹配时， Django在views.py中查找函数index()并将请求对象传递给这个视图函数
>
> 这里不需要处理任何数据，因此这个函数只包含调用render()的代码
>
> 这里向函数render()提供了两个实参：原始请求对象以及一个可用于创建网页的模板

> ①处——导入与所需数据相关联的模型
>
> ②处——函数zhuti()包含一个形参： Django从服务器接收到的request对象
>
> ③处——查询数据库，请求 ‘Topic’ 对象，并按属性 ‘date_added’ 进行排序。将返回的查询集存储到topics
>
> ④处——定义了一个将要发送给模板的上下文
>
> > 上下文是一个字典，其中的键是将在模板中用来访问数据的名称，而值是要发送给模板的数据
> >
> > 这里只有一个键—值对，它包含将在网页中显示的一组主题
>
> ⑤处——创建使用数据的网页时，除对象request和模板的路径外，还要将变量context传递给render()
>
> 6处——导入函数login_required()
>
> > 将login_required()作为装饰器用于视图函数topics()
> >
> > > 在前面加上符号@和login_required，让Python在运行topics()的代码前先运行login_required()的代码
>
> 7处——login_required()的代码检查用户是否已登录，仅当用户已登录时， Django才运行topics()的代码
>
> 如果用户未登录，就重定向到登录页面
>
> > 为实现重定向，需要修改settings.py，让Django知道到哪里去查找登录页面
>
> 8处——用户登录后， request对象将有一个user属性，这个属性存储了有关该用户的信息
>
> > ***Topic.objects.filter(owner=request.user)***让Django只从数据库中获取owner属性为当前用户的Topic对象
> >
> > > 由于没有修改主题的显示方式，因此无需对页面topics的模板做任何修改
> >
> > 要查看结果，以所有既有主题关联到的用户的身份登录，并访问topics页面，将看到所有的主题
> >
> > 然后，注销并以另一个用户的身份登录， topics页面将不会列出任何主题

```python
@login_required
def topic(request,topic_id):										# ①
    """显示单个主题的所有文章"""
    topic = Topic.objects.get(id=topic_id)							# ②
    if topic.owner != request.user:									# 6
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')				# ③
    context = {'topic':topic,'entries':entries}						# ④
    return render(request,'yj_logs/topic.html',context)				# ⑤
```

>①处——第一个除request对象外还包含另一个形参的视图函数
>
>> 这个函数接受正则表达式(?P<topic_id>\d+)捕获的值，并将其存储到topic_id中
>
>②处——使用get()来获取指定的主题，就像前面在Django shell中所做的那样
>
>③处——获取与该主题相关联的条目，并将它们按date_added排序
>
>> *date_added前面的减号指定按降序排列，即先显示最近的条目*
>
>④处——将主题和条目都存储在字典context中
>
>⑤处——将字典context发送给模板topic.html

>***②处和③处的代码被称为查询，因为它们向数据库查询特定的信息***
>
>***在自己的项目中编写这样的查询时，先在Django shell中进行尝试大有裨益***
>
>***相比于编写视图和模板，再在浏览器中检查结果，在shell中执行代码可更快地获得反馈***
>
>先导入异常Http404，并在用户请求它不能查看的主题时引发这个异常
>
>收到主题请求后，在渲染网页前检查该主题是否属于当前登录的用户
>
>6处——如果请求的主题不归当前用户所有，就引发Http404异常，让Django返回一个404错误页面

```python
@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':							  			# ①
        # GET未提交数据：创建一个新表单
        form = TopicForm()									  			# ②
    else:
        # POST提交了数据，对数据进行处理
        form = TopicForm(request.POST)						  			# ③
        if form.is_valid():												# ④
            new_topic = form.save(commit=False)							# ⑤	7
            new_topic.owner = request.user								#    8
            new_topic.save()							  				#    9
            return HttpResponseRedirect(reverse('yj_logs:topics'))		# ⑥

    context = {'form':form}
    return render(request,'yj_logs/new_topic.html',context)
```

> 导入了HttpResponseRedirect类，用户提交主题后使用这个类将用户重定向到网页topics
>
> 函数reverse()根据指定的URL模式确定URL，这意味着Django将在页面被请求时生成URL
>
> 还导入了刚才创建的表单TopicForm
>
> ***GET请求和POST请求***
>
> > 创建Web应用程序时，将用到的两种主要请求类型是GET请求和POST请求
> >
> > > GET请求——对于只是从服务器读取数据的页面，使用GET请求
> > >
> > > POST请求——在用户需要通过表单提交信息时，通常使用POST请求
> >
> > 处理所有表单时，都指定使用POST方法，还有一些其他类型的请求，但这个项目没有使用
>
> 函数new_topic()将请求对象作为参数
>
> 用户初次请求该网页时，其浏览器将发送GET请求；用户填写并提交表单时，其浏览器将发送POST请求
>
> 根据请求的类型可以确定用户请求的是空表单（GET请求）还是要求对填写好的表单进行处理（POST请求）
>
> ①处——确定请求方法是GET还是POST
>
> > 如果请求方法不是POST，请求就可能是GET，因此需要返回一个空表单
> >
> > （即便请求是其他类型的，返回一个空表单也不会有任何问题）
>
> ②处——创建一个TopicForm实例，将其存储在变量form中，
>
> > 再通过⑦处上下文字典将这个表单发送给模板
> >
> > 由于实例化TopicForm时没有指定任何实参， Django将创建一个可供用户填写的空表单
>
> 如果请求方法为POST，将执行else代码块，对提交的表单数据进行处理
>
> ③处——使用用户输入的数据（它们存储在request.POST中）创建一个TopicForm实例 
>
> > 这样对象form将包含用户提交的信息
>
> ④处——要将提交的信息保存到数据库，必须先通过检查确定它们是有效的
>
> > 函数is_valid()核实用户填写了所有必不可少的字段（表单字段默认都是必不可少的）
> >
> > 且输入的数据与要求的字段类型一致（例如，字段text少于200个字符，这是在models.py中指定的）
>
> ⑤处——如果所有字段都有效，就调用save()将表单中的数据写入数据库
>
> > 保存数据后，就可离开这个页面了
>
> ⑥处——使用reverse()获取页面topics的URL，并将其传递给HttpResponseRedirect()
>
> > HttpResponseRedirect()将用户的浏览器重定向到页面topics
> >
> > 在页面topics中，用户将在主题列表中看到他刚输入的主题
>
> 7处——首先调用form.save()，并传递实参commit=False
>
> > 因为要先修改新主题，再将其保存到数据库中
>
> 8处——将新主题的owner属性设置为当前用户
>
> 9处——对刚定义的主题实例调用save()
>
> > 现在主题包含所有必不可少的数据，将被成功地保存

```python
@login_required
def new_entry(request,topic_id):
    """在特定的主题中添加新文章"""
    topic = Topic.objects.get(id=topic_id)								# 1

    if request.method != 'POST':										# 2
        # GET——未提交数据，创建一个新表单
        form = EntryForm()												# 3
    else:
        # POST——提交了数据，对数据进行处理
        form = EntryForm(data=request.POST)								# 4
        if form.is_valid():
            new_entry = form.save(commit=False)							# 5
            new_entry.topic = topic										# 6
            new_entry.save()
            return HttpResponseRedirect(reverse('yj_logs:topic',		# 7
                                                args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,'yj_logs/new_entry.html',context)
```

> 1处——渲染页面以及处理表单数据时需要知道针对的是哪个主题
>
> > 使用topic_id来获得正确的主题
>
> 2处——检查请求方法是POST还是GET
>
> 3处——GET请求执行if代码块：
>
> > 创建一个空的EntryForm实例
>
> 4处——POST请求就对数据进行处理：
>
> > 创建一个EntryForm实例，使用request对象中的POST数据来填充它
>
> 5处——调用save()并传递实参commit=False 
>
> > 让Django创建一个新的条目对象，并将其存储到new_entry中，但不将它保存到数据库中
>
> 6处——将new_entry的属性topic设置为在这个函数开头从数据库中获取的主题 
>
> > 然后调用save()，且不指定任何实参
> >
> > 这将把条目保存到数据库，并将其与正确的主题相关联
>
> 7处——将用户重定向到显示相关主题的页面
>
> > 调用reverse()时，需要提供两个实参：
> >
> > > reverse()——要根据它来生成URL的URL模式的名称；
> > >
> > > 列表args——其中包含要包含在URL中的所有实参
> > >
> > > > 在这里，列表args只有一个元素——topic_id
> >
> > 接下来，调用HttpResponseRedirect()将用户重定向到显示新增条目所属主题的页面

```python
@login_required
def edit_entry(request,entry_id):
    """编辑既有文章"""
    entry = Entry.objects.get(id=entry_id)								# 1
    topic = entry.topic
    if topic.owner != request.user:										# 6
        raise Http404

    if request.method != 'POST'
        # 初次请求，使用当前文章填充表单
        form = EntryForm(instance=entry)								# 2
    else:
        # POST提交的请求，对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)				# 3
        if form.is_valid():
            form.save()													# 4
            return HttpResponseRedirect(reverse('yj_logs:topic',		# 5
                                                args=[topic.id]))

    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'yj_logs/edit_entry.html',context)
```

> 1处——获取用户要修改的文章对象，以及与该文章相关联的主题
>
> 2处——请求方法为GET时执行if代码块
>
> > 使用实参instance=entry创建一个EntryForm实例
> >
> > 这个实参让Django创建一个表单，并使用既有文章对象中的信息填充它
> >
> > 用户将看到既有的数据，并能够编辑它们
>
> 3处——处理POST请求时
>
> > 传递实参instance=entry和data=request.POST
> >
> > > 让Django根据既有文章对象创建一个表单实例，并根据request.POST中的相关数据对其进行修改
>
> 4处——检查表单是否有效，如果有效，就调用save()，且不指定任何实参
>
> 5处——重定向到显示文章所属主题的页面，用户将在其中看到其编辑的文章的新版本
>
> 6处——检查主题的所有者是否是当前登录的用户：如果不是，就引发Http404异常



















