# 在 Django 中创建项目（虚拟环境）

## 第一步——创建项目和应用程序

### 一、安装Django：

```shell
pip install Django
```

### 二、新建一个项目：

```shell
1.django-admin.py startproject yj_log .		##让Django新建一个名为yj_log的项目
2.ls
  ... manage.py  yj_log
3.ls yj_log
  ... __init__.py  __pycache__  settings.py  urls.py  wsgi.py
```

>1.末尾的句点让新项目使用合适的目录结构，这样开发完成后可轻松地将应用程序部署到服务器
>
>> 千万别忘了这个句点，否则部署应用程序时将遭遇一些配置问题
>>
>> 如果忘记了，就将创建的文件和文件夹删除（ll_env除外），再重新运行这个命令
>
>2.命令ls（Win为dir）
>
>> 表明Django新建了一个名为yj_log的目录，它还创建了一个名为manage.py的文件，这是一个简单的程序，它接受命令并将其交给Django的相关部分去运行，将使用这些命令来管理诸如使用数据库和运行服务器等任务
>
>3.目录learning_log包含4个文件，其中最重要的是
>
>> settings.py——指定Django如何与系统交互以及如何管理项目，开发项目过程中将修改并添加一些设置
>>
>>  urls.py——告诉Django应创建哪些网页来响应浏览器请求
>>
>> wsgi.py——帮助Django提供它创建的文件，是Yweb server gateway interface（Web服务器网关接口）的首字母缩写

### 三、创建数据库

>网站需要从某个地方获取数据才能显示出来，通常来说这个地方就是数据库
>
>写好的网站文件保存在数据库里，当用户访问该网站时，Django 就去数据库里把数据取出来展现给用户
>
>Django将大部分与项目相关的信息都存储在数据库中，因此需要创建一个供Django使用的数据库
>
>为给项目“Yj_log”创建数据库，在处于活动虚拟环境中的情况下执行下面的命令：

```shell
1.python manage.py migrate
2.ls
  ... db.sqlite3  manage.py  yj_log
```

### 四、查看项目

> 核实Django是否正确地创建了项目

```shell
1.python manage.py runserver
  >>> Performing system checks...

  ... System check identified no issues (0 silenced).			##①
  ... May 22, 2017 - 08:30:55
  ... Django version 1.11.1, using settings 'Yj_log.settings'	##②
  ... Starting development server at http://127.0.0.1:8000/		##③
  ... Quit the server with CONTROL-C
```

>Django启动一个服务器，能够查看系统中的项目，了解它们的工作情况
>
>当在浏览器中输入URL以请求网页时，该Django服务器将进行响应：
>
>> 生成合适的网页，并将其发送给浏览器
>
>①处， Django通过检查确认正确地创建了项目
>
>②处，指出了使用的Django版本以及当前使用的设置文件的名称
>
>③处，项目的URL——http://127.0.0.1:8000/表明项目将在本机（即localhost）的端口8000上侦听请求
>
>> localhost是一种只处理当前系统发出的请求，而不允许其他任何人查看你正在开发的网页的服务器

### 五、创建应用程序

> Django项目由一系列应用程序组成，它们协同工作，让项目成为一个整体
>
> 现在暂时只创建一个应用程序，它将完成项目的大部分工作。后续将再添加一个管理用户账户的应用程序
>
> 在前面打开的终端窗口中还运行着runserver
>
> 再打开一个终端窗口（或标签页），并切换到manage.py所在的目录。进入虚拟环境，执行命令startapp：

```shell
1.workon YL-env
2.python manage.py startapp yj_logs
3.ls
  ... db.sqlite3  manage.py  yj_log  yj_logs
4.ls yj_logs
  ... admin.py  apps.py  __init__.py  models.py  __pycache__  tests.py  views.py
```

> 2.命令 startapp \<appname\> 让Django建立创建应用程序所需的基础文件
>
> 3.如果现在查看项目目录，将看到其中新增了一个文件夹yj_logs
>
> 这个文件夹中最重要的文件是
>
> > models.py——定义要在应用程序中管理的数据
> >
> > admin.py
> >
> > views.py

##### 1、定义模型——/yj_logs/models.py

> 每位用户都需要在学习笔记中创建很多主题
>
> 用户输入的每个条目都与特定主题相关联，这些条目将以文本的方式显示
>
> 还需要存储每个条目的时间戳，以便能够告诉用户各个条目都是什么时候创建的

> **models.py**
>
> > 导入了模块models，提示创建自己的模型
> >
> > 模型告诉Django如何处理应用程序中存储的数据
> >
> > 在代码层面，模型就是一个类，像每个类一样包含属性和方法

##### 2、激活模型——/yj_log/settings.py

>要使用模型，必须让Django将应用程序包含到项目中
>
>打开settings.py（yj_log文件夹中）：INSTALLED_APPS列表告诉Django哪些应用程序安装在项目中
>
>> INSTALLED_APPS告诉Django项目是由哪些应用程序组成，将前面的应用程序yj_logs添加到这个列表

### 六、ROOT管理网站

> 为应用程序定义模型时， Django提供的管理网站（admin site）能够轻松地处理模型
>
> 网站的管理员可使用管理网站，但普通用户不能使用
>
> > Django允许创建root用户。权限决定了用户可执行的操作
> >
> > 最严格的权限设置只允许用户阅读网站的公开信息
> >
> > 注册了的用户通常可阅读自己的私有数据，还可查看一些只有会员才能查看的信息
> >
> > 而为有效地管理Web应用程序，网站所有者通常需要访问网站存储的所有信息
> >
> > 优秀的管理员会小心对待用户的敏感信息，因为用户对其访问的应用程序有极大的信任
>
> 建立管理网站，并通过它使用模型Topic来添加一些主题：

##### 1、创建超级用户

```shell
1.python manage.py createsuperuser
  ... Username (leave blank to use 'yj'): YJ1516	##设置root用户，留空默认为'yj'
  ... Email address: 								##邮箱，可不写
  ... Password: 									##root密码
  ... Password (again): 							##重复密码
  ... Superuser created successfully.				##成功创建root用户
```

> Django并不存储密码，而存储从该密码派生出来的一个字符串——散列值
>
> 每当输入密码时， Django都计算其散列值，并将结果与存储的散列值进行比较
>
> 如果这两个散列值相同，就通过了身份验证
>
> 通过存储散列值，即便黑客获得了网站数据库的访问权，也只能获取其中存储的散列值，而无法获得密码
>
> 在网站配置正确的情况下，几乎无法根据散列值推导出原始密码

### 七、定义模型 “Topic” 和 “Entry”——/yj_logs/models.py

> 要使用yj_logs，需要为用户可在yj_logs中添加的条目定义模型
>
> 每个条目都与特定主题相关联，这种关系被称为多对一关系，即多个条目可关联到同一个主题

##### 1、迁移模型

> 由于添加了新模型 “Topic” 和 “Entry” ，因此需要迁移数据库：
>
> > 修改了 models.py 
> >
> > 执行命令 python manage.py makemigrations app_name 
> >
> > 再执行命令 python manage.py migrate

```shell
1.python manage.py makemigrations yj_logs
  ... Did you rename topic.date_added to topic.date (a DateTimeField)? [y/N] y
  ... Did you rename topic.text to topic.name (a CharField)? [y/N] y   # 如有修改提示是否保存
  ... Migrations for 'yj_logs':										   # 迁移 'yj_logs'
    ... yj_logs/migrations/0002_auto_20170523_1716.py		# 新迁移文件和更改的详细信息
          - Create model Entry
          - Rename field date_added on topic to date
          - Rename field text on topic to name
          - Add field topic to entry
2.python manage.py migrate
  ... Operations to perform:		# 执行操作：
        Apply all migrations: admin, auth, contenttypes, sessions, yj_logs	  # 应用所有迁移
  ... Running migrations:			# 运行迁移：
        Applying yj_logs.0002_auto_20170523_1716... OK
```

> 命令makemigrations让Django确定该如何修改数据库，使其能够存储与定义的新模型相关联的数据
>
> 迁移文件将在数据库中为各个模型创建一个表

> 每当需要修改“yj_logs”管理的数据时，都采取如下三个步骤：
>
> > 1.修改models.py
> >
> > 2.对yj_logs调用makemigrations
> >
> > 3.让Django迁移项目

##### 2、向ROOT网站注册 “Topic” 和 “Entry” ——/yj_logs/admin.py

> Django自动在管理网站中添加了一些模型，如 “用户” 和 “组” ，但对于后来创建的模型，必须手工进行注册
>
> 在admin.py文件中进行注册——类似类的引用
>
> 注册完后，返回到[yj_logs](http://localhost/admin/)，会看到YJ_LOGS下列出了 “主题” 和 “记录” 两个选项（因为起了中文别名）

##### 3、添加文章

> 向管理网站注册 “Topic” 和 “Entry” 后，可以添加文章
>
> 单击 ”记录“ 进入网页，它几乎是空的，这是因为还没有添加任何文章
>
> 单击增加，将看到一个用于添加新文章的表单

##### 4、Django shell

> 输入一些数据后，就可通过交互式终端会话以编程方式查看这些数据了，这种交互式环境称为Django shell
>
> 是测试项目和排除其故障的理想之地

```shell
1.python manage.py shell
>>> from yj_logs.models import 主题			 # ①
>>> 主题.objects.all()
  <QuerySet [<主题: 攀岩>, <主题: 围棋>]>
>>> topics = 主题.objects.all()				 # ②
>>> for topic in topics:	                  # ③
... print(topic.id, topic)					  # ④
...
  1.攀岩
  2.围棋
```

> 在虚拟环境中执行命令python manage.py shell启动一个Python解释器
>
> 可使用它来探索存储在项目数据库中的数据
>
> ①——导入模块**yj_logs.models**中的模型**主题**，然后使用方法**主题.objects.all()**来获取该模型的所有实例
>
> > 它返回的是一个列表，称为查询集（queryset）
>
> ②③④——遍历查询集，查看分配给每个主题对象的ID
>
> > ②——将返回的查询集存储在topics中
> >
> > ③——遍历查询集
> >
> > ④——打印每个主题的id属性和字符串表示
>
> 从输出可知，主题**攀岩**的**ID**为1，而**围棋**的**ID**为2

> 知道对象的ID后，就可获取该对象并查看其任何属性——查看主题**攀岩**的属性name和date：

```shell
1.t = 主题.objects.get(id=1)
2.t.name
  '攀岩'
3.t.date
  datetime.datetime(2017, 5, 23, 2, 43, 34, 379795, tzinfo=<UTC>)
```

> 还可以查看与主题相关联的条目
>
> 给模型 “文章” 定义了属性 “文章题目”，这是一个ForeignKey，将条目与主题关联起来
>
> 利用这种关联， Django能够获取与特定主题相关联的所有条目：

```sh
1.t.文章_set.all()
```

### 八、创建网页——yj_logs的主页

> 使用Django创建网页的过程通常分三个阶段：
>
> > 1.定义URL模式——
> >
> > > URL模式描述了URL如何设计，让Django知道如何将浏览器请求与网站URL匹配，以确定返回哪个网页
> >
> > 2.编写视图函数——
> >
> > >每个URL都被映射到特定的视图——视图函数获取并处理网页所需的数据
> >
> > 3.编写模板——
> >
> > >视图函数通常调用一个模板，后者生成浏览器能够理解的网页

##### 1、定义URL模式，映射URL——/yj_logs/urls.py

> 用户通过在浏览器中输入URL以及单击链接来请求网页，因此需要确定项目需要哪些URL
>
> 主 页 的 URL 最 重 要 ， 它 是 用 户 用 来 访 问 项 目 的 基 础 URL 
>
> 当 前 ， [基 础 URL](http://localhost:8000/)返回默认的Django网站
>
> 修改这一点，将这个基础URL映射到 “yj_logs” 的主页
>
> [urls.py的官方文档](https://docs.djangoproject.com/en/1.11/topics/http/urls/)

> 1.在/yj_logs/urls.py中包含yj_logs的URL
>

##### 2、编写视图函数——/yj_logs/views.py

> 视图函数接受请求中的信息，准备好生成网页所需的数据，再将这些数据发送给浏览器——这通常是使用定
>
> 义了网页是什么样的模板实现的

##### 3、编写模板——/yj_logs/templates/yj_logs/index.html

> 模板定义了网页的结构，指定了网页是什么样的，而每当网页被请求时， Django将填入相关的数据
>
> 模板让用户能够访问视图提供的任何数据
>
> yj_logs的主页视图没有提供任何数据，因此相应的模板非常简单

> 在文件夹yj_logs中新建一个文件夹，并将其命名为templates
>
> 在templates中，再新建一个文件夹，并将其命名为yj_logs
>
> 这好像有点多余，但建立了Django能够明确解读的结构，即便项目很大，包含很多应用程序亦如此
>
> 在 **/yj_logs/templates/yj_logs/** 中新建一个index.html文件，在这个文件中编写模板

### 九、创建其他网页

> 将创建两个网页，其中一个列出所有的主题，另一个显示特定主题的所有条目
>
> 对于每个网页都将指定URL模式，编写一个视图函数，并编写一个模板
>
> 但在此之前先创建一个**父模板**，项目中的其他模板都将继承它

##### 1、模板继承

**_模板继承的优点：_**

> 在子模板中，只需包含当前网页特有的内容，这不仅简化了每个模板，还使得网站修改起来容易得多
>
> 要修改很多网页都包含的元素，只需在父模板修改该元素，所做的修改将传导到继承该父模板的每个页面
>
> 在包含数十乃至数百个网页的项目中，这种结构使得网站改进起来容易而且快捷得多

> 创建网站时，几乎都有一些所有网页都将包含的元素
>
> 因此可编写包含通用元素的父模板，让每个网页都继承这个模板而不必在每个网页中重复定义这些通用元素

###### 父模板——/yj_logs/templates/yj_logs/base.html

>首先创建一个名为**base.html**的模板，并将其存储在index.html所在的目录中
>
>这个文件包含所有页面都有的元素，其他模板都继承base.html
>
>当前，所有页面都包含的元素只有顶端的标题
>
>要在每个页面中包含这个模板，因此将这个标题设置为到主页的链接

###### 子模板

>现在需要重写index.html，使其继承父模板base.html——index.html

> _大型项目中，通常有一个用于整个网站的父模板——base.html，且网站的每个主要部_
>
> _分都有一个父模板。每个部分的父模板都继承base.html，而网站的每个网页都继承相应_
>
> _部分的父模板。这让开发者能够轻松地修改整个网站的外观、网站任何一部分的外观以及任_
>
> _何一个网页的外观。这种配置提供了一种效率极高的工作方式_

##### 2、显示所有主题的页面

###### 1、URL模式——yj_logs/urls.py

>首先定义显示所有题目的页面的URL
>
>通常使用一个简单的URL片段来指出网页显示的信息，使用 “topic” 作为区分
>
>因此URL http://localhost:8000/topic/ 将返回显示所有题目的页面
>
>修改yj_logs/urls.py

###### 2、视图函数——yj_logs/views.py

>函数 zhuti() 需要从数据库中获取一些数据，并将其发送给模板
>
>需要在views.py中添加topics()函数

###### 3、模板——/yj_logs/templates/yj_logs/topics.html

>显示所有主题的页面的模板topics.html接受字典context，以便能够使用topics()提供的数据

**写完topics.html后需要修改父模板，使其包含到显示所有主题的页面的链接**

##### 3、显示特定主题的页面

###### 1、URL模式——yj_logs/urls.py

>显示特定主题的页面的URL模式与前面的所有URL模式都稍有不同
>
>它将使用主题的id属性来指出请求的是哪个主题
>
>例如，如果用户要查看主题Chess（其id为1）的详细页面， [其URL是](http://localhost:8000/topics/1/)

###### 2、视图函数——在yj_logs/views.py创建topic()视图函数

>函数topic()需要从数据库中获取指定的主题以及与之相关联的所有条目

###### 3、模板——/yj_logs/templates/yj_logs/topic.html

> 这个模板需要显示主题的名称和主题下的文章；如果当前主题不包含任何内容，需向用户指出这一点

###### 4、将显示所有主题的页面的每个主题都设置为链接——/yj_logs/templates/yj_logs/topics.html

> 在浏览器中查看显示特定主题的页面前，需要修改模板topics.html，让每个主题都链接到相应的网页

---

## 第二步——用户账户

> Web应用程序的核心是让任何用户都能够注册账户并能够使用它，不管用户身处何方
>
> 接下来将创建一些表单：
>
> > 让用户能够添加主题和条目，以及编辑既有的条目
>
> 还将学习Django如何防范对基于表单的网页发起的攻击，因此无需花太多时间考虑确保应用程序安全的问题
>
> 然后将实现一个用户身份验证系统：
>
> > 创建一个注册页面，供用户创建账户，并让有些页面只能供已登录的用户访问

接下来修改一些视图函数，使得用户只能看到自己的数据。
确保用户数据的安全

### 一、让用户能够输入数据

> 建立用于创建用户账户的身份验证系统之前，先添加几个页面，让用户能够输入数据
>
> 用户能够添加新主题、添加新文章以及编辑既有条目
>
> 当前，只有超级用户能够通过管理网站输入数据
>
> 应禁止用户与管理网站交互，因此将使用Django的表单创建工具来创建让用户能够输入数据的页面

##### 1、添加新主题

> 首先来让用户能够添加新主题
>
> 创建基于表单的页面的方法几乎与前面创建网页一样：
>
> > 定义一个URL，编写一个视图函数并编写一个模板
>
> 主要差别是需要导入包含表单的模块forms.py

###### 用于添加新主题的表单——/yj_logs/forms.py

> 能让用户输入并提交信息的页面都是表单，哪怕它看起来不像表单
>
> 用户输入信息时需要验证，确认提供的信息是正确的数据类型，且不是恶意的信息，如中断服务器的代码
>
> 然后再对有效信息进行处理，并将其保存到数据库的合适地方
>
> 这些工作很多都是由Django自动完成的
>
> 在Django中，创建表单的最简单方式是使用ModelForm，它根据模型中的信息自动创建表单
>
> 创建一个名为forms.py的文件，将其存储到models.py所在的目录中，并在其中编写第一个表单

###### URL模式new_topic——/yj_logs/urls.py

> 这个新网页的URL应简短而具有描述性，因此当用户要添加新主题时，我们将切换到[new_topic](http://localhost:8000/new_topic/)
>
> 添加网页new_topic的URL模式到yj_logs/urls.py中
>
> 这个URL模式将请求交给视图函数new_topic()

###### 视图函数new_topic()——/yj_logs/views.py

> 函数new_topic()需要处理两种情形：
>
> > 1.刚进入new_topic网页（在这种情况下，它应显示一个空表单）
> >
> > 2.对提交的表单数据进行处理，并将用户重定向到网页topics

###### 模板——/yj_logs/templates/yj_logs/new_topic.html

> 显示刚创建的表单

###### 链接到页面new_topic——/yj_logs/templates/yj_logs/topics.html

> 在页面topics中添加一个到页面new_topic的链接

##### 2、添加新文章

###### 用于添加新文章的表单——/yj_logs/forms.py

> 创建一个与模型Entry相关联的表单，这个表单的定制程度比TopicForm要高些

###### URL模式new_entry——/yj_logs/urls.py

> 用于添加新文章的页面的URL模式中，需要包含实参topic_id，因为文章必须与特定的主题相关联

###### 视图函数new_entry()——/yj_logs/views.py

###### 模板——/yj_logs/templates/yj_logs/new_entry.html

###### 链接到页面new_entry——/yj_logs/templates/yj_logs/topic.html

> 在显示特定主题的页面topic.html中添加到页面new_entry的链接

##### 3、编辑既有文章

###### URL模式edit_entry——/yj_logs/urls.py

> 这个页面的URL需要传递要编辑的条目的ID

###### 视图函数edit_entry()——/yj_logs/views.py

> 页面edit_entry收到GET请求时， edit_entry()将返回一个表单，让用户能够对条目进行编辑
>
> 该页面收到POST请求（文章文本经过修订）时将修改后的文本保存到数据库中

###### 模板——/yj_logs/templates/yj_logs/edit_entry.html

###### 链接到页面edit_entry——/yj_logs/templates/yj_logs/topic.html

> 在显示特定主题的页面topic.html中给每个文章添加到页面edit_entry的链接



***至此，“yj_logs”已具备了需要的大部分功能：***

> ***用户可添加主题和文章，还可根据需要查看任何一组文章***

***下一节实现一个用户注册系统，让任何人都可向“yj_logs”申请账户，并创建自己的主题和文章***

### 二、创建用户账户

> 建立一个用户注册和身份验证系统，让用户能够注册账户，进而登录和注销
>
> > 1、创建一个新的应用程序，其中包含与处理用户账户相关的所有功能
> >
> > 2、对模型Topic稍做修改，让每个主题都归属于特定用户

##### 1、应用程序users

###### 使用命令startapp来创建一个名为users的应用程序，其目录结构与应用程序yj_logs相同

> python manage.py startapp users

###### 将应用程序users添加到settings.py中——/yj_log/settings.py

> 以让Django将应用程序users包含到项目中

##### 2、包含应用程序users的URL

###### 修改项目根目录的urls.py——/yj_log/urls.py

> 包含将为应用程序users定义的URL

##### 3、实现登录页面的功能

> 使用Django提供的默认登录视图，因此URL模式会稍有不同
>
> 新建一个名为urls.py的文件，并在其中添加代码——/log/users/urls.py

###### 登陆页面的模板login.html——/users/templates/users/login.html

>用户请求登录页面时， Django将使用其默认视图login，但需要为这个页面提供模板
>
>为此，在目录log/users/中，创建一个名为templates的目录，并在其中创建一个名为users的目录

###### 链接到登录页面——/yj.logs/base.html

> 在base.html中添加到登录页面的链接，让所有页面都包含它
>
> 用户已登录时不显示这个链接，因此将它嵌套在一个{% if %}标签中

###### 使用登录页面

> 前面建立了一个用户账户，下面来登录一下，看看登录页面是否管用
>
> 访问[admin](http://localhost:8000/admin/)，如果依然是以管理员的身份登录的，在页眉上注销
>
> 注销后，访问[login](http://localhost:8000/users/login/)，将看到登录页面
>
> > 输入设置的用户名和密码，将进入页面index
> >
> > 在这个主页的页眉中，显示了一条个性化问候语，其中包含用户名

##### 4、实现注销功能

> 需要提供一个让用户注销的途径
>
> 不创建用于注销的页面，而让用户只需单击一个链接就能注销并返回到主页
>
> 为此为注销链接定义一个URL模式，编写一个视图函数，并在base.html中添加一个注销链接

###### 注销页面的URL模式——/users/urls.py

###### 视图函数logout_view()——/users/views.py

> 函数logout_view()很简单：只是导入Django函数logout()，并调用它，再重定向到主页

###### 链接到注释视图——/yj.logs/base.html

> 在base.html中添加一个注销链接，让每个页面都包含它
>
> 将它放在标签{% if user.is_authenticated %}中，使得仅当用户登录后才能看到它

##### 5、实现注册功能

> 创建一个让新用户能够注册的页面
>
> 使用Django提供的表单UserCreationForm，但编写自己的视图函数和模板

###### 注册页面的URL模式——/users/urls.py

###### 视图函数register()————/users/views.py

> 首次请求注册页面时，register()显示一个空的注册表单，并在用户提交填写好的注册表单时对其进行处理
>
> 如果注册成功，这个函数还需让用户自动登录

###### 注册页面的模板register.html——/users/templates/users/register.html

> 务必要和login.html的目录相同

###### 链接到注册页面——/yj.logs/base.html

> 在用户没有登录时显示到注册页面的链接

### 三、用户专属数据

> 对一些页面进行限制，仅让已登录的用户访问它们，并确保每个主题都属于特定用户
>
> 用户应该能够输入其专有的数据：
>
> > 创建一个系统，确定各项数据所属的用户，再限制对页面的访问，让用户只能使用自己的数据
>
> 修改模型Topic，让每个主题都归属于特定用户：
>
> > 这也将影响文章，因为每个文章都属于特定的主题

##### 1、使用装饰器@login_required限制访问

> Django提供了装饰器@login_required，能够实现：
>
> > 对于某些页面，只允许已登录的用户访问它们
>
> 装饰器（decorator）是放在函数定义前面的指令， Python在函数运行前根据它来修改函数代码的行为

###### 限制对topics页面的访问——yj_logs/views.py

> 每个主题都归特定用户所有，因此应只允许已登录的用户请求topics页面

###### 若用户未登录进行重定向到登陆页面——/yj_log/settings.py

> 现在，如果未登录的用户请求装饰器@login_required的保护页面，
>
> Django将重定向到settings.py中的LOGIN_URL指定的URL

##### 2、全面限制对项目'yj_log'的访问

> 确定项目的哪些页面不需要保护，再限制对其他所有页面的访问
>
> 可以修改过于严格的访问限制，其风险比不限制对敏感页面的访问更低

> 项目“yj_log”将不限制对主页、注册页面和注销页面的访问，并限制对其他所有页面的访问

###### 对除index()外的每个视图都应用装饰器@login_required——/yj_logs/views.py

> 如果用户在未登录的情况下尝试访问这些页面，将被重定向到登录页面
>
> 还不能单击到new_topic等页面的链接。但如果你输入[URL](http://localhost:8000/new_topic/)，将重定向到登录页面
>
> 对于所有与私有用户数据相关的URL，都应限制对它们的访问

##### 3、将数据关联到用户

> 现在将数据关联到提交它们的用户
>
> 只需将最高层的数据关联到用户，这样更低层的数据将自动关联到用户
>
> > 例如，在项目“yj_log”中，应用程序的最高层数据是主题，而所有文章都与特定主题相关联
> >
> > 只要每个主题都归属于特定用户，就能确定数据库中每个文章的所有者

###### 修改模型Topic：

>在其中添加一个关联到用户的外键：

> > 修改后必须对数据库进行迁移
> >
> > 最后必须对有些视图进行修改，使其只显示与当前登录的用户相关联的数据

###### 确定当前有哪些用户——启动一个Django shell会话，并执行：

> 迁移数据库时， Django将对数据库进行修改，使其能够存储主题和用户之间的关联
>
> 为执行迁移， Django需要知道该将各个既有主题关联到哪个用户
>
> > 最简单的办法是，将既有主题都关联到同一个用户，如超级用户，为此需要知道该用户的ID

```shell
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ python manage.py shell		# 1
>>> from django.contrib.auth.models import User								# 2
>>> User.objects.all()														# 3
<QuerySet [<User: YJ1516>, <User: yj>]>
>>> for user in User.objects.all():											# 4
...     print(user.username,user.id)
... 
YJ1516 1
yj 2
```

>1处——启动一个Django shell会话
>
>2处——在shell会话中导入模型User
>
>3处——查看目前为止创建了哪些用户
>
>> 分别为用户YJ1516和用户yj
>
>4处——遍历用户列表并打印每位用户的用户名和ID
>
>> Django询问要将既有主题关联到哪个用户时指定其中的一个ID值

###### 迁移数据库——1、2、3

> 根据用户ID迁移数据库：

###### 1-创建迁移文件：

```bash
$ python manage.py makemigrations yj_logs											# 1
You are trying to add a non-nullable field 'owner' to topic without a default; 		# 2
we can't do that (the database needs something to populate existing rows).
Please select a fix:																# 3
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1																	# 4
Please enter the default value now, as valid Python									# 5
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 1																				# 6
Migrations for 'yj_logs':
  yj_logs/migrations/0005_topic_owner.py
    - Add field owner to topic
```

> 1处——执行命令makemigrations
>
> 2处——Django指出试图给既有模型Topic添加一个必不可少（不可为空）的字段，而该字段没有默认值
>
> 3处——Django提供了两种选择：要么现在提供默认值，要么退出并在models.py中添加默认值
>
> 4处——选择第一个选项
>
> 5处——因此Django提示输入默认值（用户的ID）
>
> 6处——将所有既有主题都关联到管理用户YJ1516，因此输入用户ID值1
>
> > 并非必须使用超级用户，而可使用已创建的任何用户的ID
>
> 接下来， Django使用这个值来迁移数据库，并生成了迁移文件0005_topic_owner.py
>
> > 它在模型Topic中添加字段owner

###### 2-迁移数据库：

```shell
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, yj_logs
Running migrations:
  Applying yj_logs.0005_topic_owner... OK
```

###### 3-验证迁移符合预期：

```shell
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ python manage.py shell			# 1
Python 3.5.2+ (default, Nov  3 2016, 11:10:16) 
[GCC 6.2.0 20161027] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from yj_logs.models import Topic											# 2
>>> for topic in Topic.objects.all()											# 3
  File "<console>", line 1
    for topic in Topic.objects.all()
                                   ^
SyntaxError: invalid syntax
>>> for topic in Topic.objects.all():
...     print(topic,topic.owner)
... 
攀岩 YJ1516
```

> 1处——进入shell环境
>
> 2处——从yj_logs.models中导入Topic
>
> 3处——遍历所有的既有主题，并打印每个主题及其所属的用户
>
> > 现在每个主题都属于用户YJ1516

###### 4-重置数据库：

> 可以重置数据库而不是迁移它，但如果这样做，既有的数据都将丢失
>
> 如果确实想要一个全新的数据库，可执行命令***python manage.py flush***，这将重建数据库的结构
>
> 这样就必须重新创建超级用户，且原来的所有数据都将丢失

##### 4、只允许用户访问自己的主题

> 当前，不管以哪个用户的身份登录，都能够看到所有的主题

###### 只向用户显示属于自己的主题——/yj_logs/views.py

##### 5、保护用户主题

> 代码没有限制对显示单个主题的页面的访问，因此**任何已登录的用户**都可输入类似[URL](http://localhost:8000/topics/1/)来访问相应主题的页面
>
> > 以拥有所有主题的用户的身份登录后访问特定的主题，并复制该页面的URL，或将其中的ID记录下来
> >
> > 然后，注销并以另一个用户的身份登录，再输入显示前述主题的页面的URL
> >
> > 虽然是以另一个用户身份登录的，但依然能够查看该主题中的文章

###### 在视图函数topic()获取请求的文章前执行检查——/yj_logs/views.py

> 服务器上没有请求的资源时，标准的做法是返回404响应
>
> 现在，如果试图查看其他用户的主题文章，将看到Django发送的消息Page Not Found

##### 6、保护用户文章edit_entry页面——/yj_logs/views.py

> 页面edit_entry的[URL](http://localhost:8000/edit_entry/entry_id/)，其中entry_id是一个数字
>
> 需要保护这个页面，禁止用户通过输入类似于前面的URL来访问其他用户的文章

##### 7、将新主题关联到当前用户

> 当前，用于添加新主题的页面没有将新主题关联到特定用户
>
> 如果尝试添加新主题，将看到错误消息IntegrityError，指出yj_logs_topic.user_id不能为NULL
>
> > 即创建新主题时必须指定其owner字段的值

###### 通过request对象获悉当前用户，将新主题关联到当前用户——/yj_logs/views.py



***现在，这个项目允许任何用户注册，而每个用户想添加多少新主题都可以***

***每个用户都只能访问自己的数据，无论是查看数据、输入新数据还是修改旧数据时都如此***

---

# 第三步——设置应用程序的样式并对其进行部署

> 设置这个项目的样式——使用Bootstrap库
>
> > 这是一组工具，用于为Web应用程序设置样式，
> >
> > 使其在任何现代设备上都看起来很专业，无论是大型的平板显示器还是智能手机
> >
> > 为此将使用应用程序django-bootstrap3，这能够练习使用其他Django开发人员开发的应用程序
>
> 将其部署到一台服务器上，让任何人都能够建立账户——把项目“log”部署到Heroku
>
> > 这个网站能够将项目推送到其服务器，让任何有网络连接的人都可使用它
> >
> > 还将使用版本控制系统Git来跟踪对这个项目所做的修改

### 一、设置项目“学习笔记”的样式——django-bootstrap3

> 使用应用程序django-bootstrap3，将其继承到项目中，为部署项目做好准备

##### 1、应用程序django-bootstrap3

> 使用django-bootstrap3来将Bootstrap继承到项目中
>
> 应用程序下载必要的Bootstrap文件放到项目的合适位置，使能够在项目的模板中使用样式设置指令

###### 安装django-bootstrap3

```shell
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ pip install django-bootstrap3
```

> 在虚拟环境下的项目目录中安装

###### 在项目中包含应用程序django-bootstrap3——/yj_log/settings.py

###### 让django-bootstrap3包含jQuery——/yj_log/settings.py

> 这是一个JavaScript库，使能够使用Bootstrap模板提供的一些交互式元素

##### 2、使用 Bootstrap 来设置项目“学习笔记”的样式

> Bootstrap是一个样式设置工具集，它提供了大量的模板，可将它们应用于项目以创建独特的总体风格
>
> 对Bootstrap初学者来说，这些模板比各个样式设置工具使用起来要容易得多
>
> 要查看Bootstrap提供的模板，可访问[getbootstrap](http://getbootstrap.com/)
>
> > 单击Getting Started，再向下滚动到Examples部分，并找到Navbars in action
>
> **使用模板Static top navbar**，它提供了简单的顶部导航条、页面标题和用于放置页面内容的容器

###### 修改base.html——1、2、3

> 修改模板base.html，以使用Bootstrap的Static top navbar模板

###### 1-定义HTML头部

> 对base.html所做的第一项修改是在这个文件中定义HTML头部
>
> > 使得显示“YJLOG-1024”的每个页面时，浏览器标题栏都显示这个网站的名称
>
> 还要添加一些在模板中使用Bootstrap所需的信息

###### 2-定义导航栏

> 定义页面顶部的导航栏

###### 3-定义页面的主要部分

> base.html的剩余部分包含页面的主要部分

###### 使用jumbotron设置主页index.html的样式

> 使用新定义的header块及另一个名为jumbotron的Bootstrap元素修改主页
>
> > jumbotron元素是一个大框，相比于页面的其他部分显得鹤立鸡群，想在其中包含什么东西都可以
> >
> > 它通常用于在主页中呈现项目的简要描述

###### 设置登录页面login.html的样式

> 改进了登录页面的整体外观，但还未改进登录表单，接下来让表单与页面的其他部分一致

###### 设置创建新主题页面new_topic.html的样式

###### 设置所有主题页面topics.html的样式

> 确保用于查看信息的页面的样式也是合适的

###### 设置主题页面topic.html中文章的样式

> topic页面包含的内容比其他大部分页面都多，因此需要做的样式设置工作要多些
>
> 使用Bootstrap面板（panel）来突出每篇文章
>
> > 面板是一个带预定义样式的div，非常适合用于显示主题的文章

### 二、部署项目——Heroku

> 将项目部署到一台服务器，让任何有网络连接的人都能够使用它
>
> > Heroku是一个基于Web的平台，让开发者能够管理Web应用程序的部署

##### 1、注册Heroku账户

##### 2、安装Herku Toolbelt

> 要将项目部署到Heroku的服务器并对其进行管理，需要使用Heroku Toolbelt提供的工具
>
> 访问[Toolbelt](https://toolbelt.heroku.com/)，根据操作系统按相关的说明安装最新的Heroku Toolbelt版本

##### 3、安装必要的包

> 还需安装很多包以帮助在服务器上支持Django项目提供的服务
>
> 在活动的虚拟环境中执行命令：

```shell
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ pip install dj-database-url
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ pip install dj-static
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ pip install static3
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ pip install gunicorn
```

> 务必逐个地执行这些命令，这样就能知道哪些包未能正确地安装
>
> > dj-database-url包帮助Django与Heroku使用的数据库进行通信
> >
> > dj-static和static3包帮助Django正确地管理静态文件
> >
> > > 静态文件包括样式规则和JavaScript文件
> >
> > gunicorn是一个服务器软件，能够在在线环境中支持应用程序提供的服务
>
> 如果安装包时出现错误也不用担心，重要的是让Heroku在部署中安装这些包

##### 4、创建包含包列表的文件requirements.txt

> Heroku需要知道项目依赖于哪些包，使用pip来生成一个文件，其中列出了这些包
>
> > 进入活动虚拟环境，并执行命令：

```shell
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ pip freeze > requirements.txt
```

> 命令freeze让pip将项目中当前安装的所有包的名称都写入到文件requirements.txt中

*requirements.txt：*

```
appdirs==1.4.3
dj-database-url==0.4.2
dj-static==0.0.6
Django==1.11.1
django-bootstrap3==8.2.3
gunicorn==19.7.1
packaging==16.8
pyparsing==2.2.0
pytz==2017.2
six==1.10.0
static3==0.7.0
```

> 项目依赖于特定版本的包，因此需要在相应的环境中才能正确地运行
>
> 部署项目时Heroku将安装requirements.txt列出的所有包从而创建一个环境，其中包含本地使用的所有包

##### 5、在包列表requirements.txt中添加psycopg2

> psycopg2帮助Heroku管理活动数据库
>
> 打开文件requirements.txt，并添加代码行**psycopg2>=2.6.1**
>
> > 这将安装2.6.1版的psycopg2，如果有更高的版本，将会安装更高的版本

##### 6、指定Python版本

> 如果没有指定Python版本Heroku将使用其当前的Python默认版本
>
> 下面确保Heroku使用开发机使用的Python版本
>
> 在活动的虚拟环境中，执行命令：

```shell
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ python --version
Python 3.5.2+
```

> 输出显示使用的Python版本为 3.5.2+
>
> 在manage.py所在的文件夹新建一个runtime.txt文件，在其中输入：

*runtime.txt：*

```
python-3.5.2+
```

> 这个文件以上面所示的格式指定了使用的Python版本
>
> 确保输入小写的python，在它后面输入一个连字符，再输入版本号

> 如果出现错误消息，指出不能使用指定的Python版本
>
> 访问[devcenter](https://devcenter.heroku.com/)并单击Python，再单击链接Specifying a Python Runtime
>
> 浏览打开的文章，了解支持的Python版本，并使用最接近的Python版本

##### 7、为部署到Heroku修改settings.py

> 需要在settings.py末尾添加一个片段，在其中指定一些Heroku环境设置

##### 8、创建启动进程的Procfile

> Procfile告诉Heroku启动哪些进程，以便能够正确地提供项目提供的服务
>
> > 这个文件只包含一行，应将其命名为Procfile（其中的P为大写）
> >
> > 不指定文件扩展名
> >
> > 并保存到manage.py所在的目录中

*Procfile：*

```
web: gunicorn yj_log.wsgi --log-file -
```

> 这行代码让Heroku将gunicorn用作服务器，并使用yj_log/wsgi.py中的设置来启动应用程序
>
> 标志log-file告诉Heroku应将哪些类型的事件写入日志

##### 9、为部署到Heroku修改wsgi.py

> 为部署到Heroku，还需修改wsgi.py，因为Heroku需要的设置与开发机使用的设置稍有不同

##### 10、创建用于存储静态文件的目录

> 在Heroku上， Django搜集所有的静态文件，并将它们放在一个地方，以便能够高效地管理它们
>
> 创建一个用于存储这些静态文件的目录
>
> > 在文件夹yj_log中新建一个名为static的文件夹，
> >
> > 在这个文件夹中创建一个名为placeholder.txt的占位文件，
> >
> > 因为项目被推送到Heroku时，它将不会包含原来为空的文件夹

##### 11、在本地使用gunicorn服务器

> Linux可在部署到Heroku前尝试在本地使用gunicorn服务器
>
> 在活动的虚拟环境中，执行命令heroku local以启动Procfile指定的进程

```

```

### 三、使用Git跟踪项目文件

> Git是一个版本控制程序，能够在每次成功实现新功能后都拍摄项目代码的快照
>
> 无论出现什么问题（如实现新功能时不小心引入了bug），都可以轻松地恢复到最后一个可行的快照
>
> 使用Git意味着在试着实现新功能时无需担心破坏项目
>
> 将项目部署到服务器时，需要确保部署的是可行版本

##### 1、安装Git并确认版本

```shell
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ sudo apt install git
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ git --version
git version 2.10.2
```

> 版本为git 2.10.2

##### 2、配置Git

> Git跟踪谁修改了项目，即便项目由一个人开发时亦如此
>
> 为进行跟踪， Git需要知道主开发者的用户名和email

```shell
(YJ-Log) log$ git config --global user.name "YJ1516"
(YJ-Log) log$ git config --global user.email "YJ1516268@outlook.com"

```

##### 3、忽略文件

> 无需让Git跟踪项目中的每个文件，因此将让Git忽略一些文件
>
> 为此，在manage.py所在的文件夹中创建一个名为.gitignore的文件，在这个文件中输入：

```
YJ-Log/
__pycache__/
*.sqlite3
```

> 忽略目录YJ-Log，因为随时都可以自动重新创建它
>
> 忽略目录\__pycache__，这个目录包含Django运行.py文件时自动创建的.pyc文件
>
> 忽略对本地数据库的修改，因为如果在服务器上使用的是SQLite，
>
> 当将项目推送到服务器时，可能会不小心用本地测试数据库覆盖在线数据库

##### 4、提交项目

> 为“时光笔记”初始化一个Git仓库，将所有必要的文件都加入到这个仓库中，并提交项目的初始状态

```shell
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ git init								  # 1
已初始化空的 Git 仓库于 /home/yj/Documents/project/log/.git/
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ git add .								  # 2
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ git commit -am "Ready for deployment"	  # 3
[master（根提交） ac8f6b4] Ready for deployment
 44 files changed, 1687 insertions(+)
 create mode 100644 .gitignore
--
......
--
 create mode 100644 yj_logs/views.py
(YJ-Log) yj@YJ-Linux:~/Documents/project/log$ git status 							  # 4
位于分支 master
无文件要提交，干净的工作区
```

> 1处——在“时光笔记”所在的目录中初始化一个空仓库
>
> 2处——将未被忽略的文件都添加到这个仓库中（千万别忘了这个句点）
>
> 3处——-a让Git在这个提交中包含所有修改过的文件，-m让Git记录一条日志消息
>
> 4处——输出表明当前位于分支master中，而工作目录是干净的
>
> > 每当要推送项目时，都希望看到这样的状态
>
> 每当项目进行了修改，都运行3、4命令将修改提交到Git仓库

##### 5、改进项目

###### 创建超级用户

> 创建超级用户来改进部署，在服务器终端：

```shell
ls											# 查看目录确保在项目目录的manage.py相同目录中
python manage.py createsuperuser			#　执行创建超级用户的命令
```

###### 确保项目安全

> 当前，部署的项目存在一个严重的安全问题：
>
> > settings.py包含设置DEBUG=True，它在发生错误时显示调试信息
>
> 开发项目时， Django的错误页面显示了重要的调试信息
>
> > 如果将项目部署到服务器后依然保留这个设置，将给攻击者提供大量可供利用的信息
>
> 需确保任何人都无法看到这些信息，也不能冒充项目托管网站来重定向请求
>
> 修改settings.py，

```python
ALLOWED_HOSTS = ['learning-log.herokuapp.com']	# 只允许Heroku托管这个项目。需要使用应用程序名称
DEBUG = False				# 用户在错误消息中看不到额外的信息，以防他们使用这些信息来攻击服务器
```

> 以能够在本地看到错误消息，但部署到服务器后不显示任何错误消息

###### 创建自定义模板404.html和500.html

###### 使用方法get_object_or_404()

> 现在如果用户手动请求不存在的主题或文章，将导致500错误
>
>  Django尝试渲染请求的页面时如果没有足够的信息来完成这项任务，将引发500错误
>
> 对于这种情形，将其视为404错误更合适，为此可使用Django快捷函数get_object_or_404()
>
> > 这个函数尝试从数据库获取请求的对象，如果这个对象不存在，就引发404异常
>
> 在views.py中导入这个函数，并用它替换函数get()：

##### 6、继续开发

> 首先对本地项目做必要的修改
>
> > 如果修改过程中创建了新文件，命令git add .（千万别忘记这个命令末尾的句点）将它们加入到Git仓库中
> >
> > 如果有修改要求迁移数据库，也需要执行这个命令，因为每个迁移都将生成新的迁移文件
>
> 然后，使用命令git commit -am "commit message"将修改提交到仓库
>
> 再使用命令git push heroku master将修改推送到Heroku
>
> 如果本地迁移了数据库，也需要迁移在线数据库
>
> > 使用一次性命令heroku run python manage.py migrate
> >
> > 也可使用heroku run bash打开一个远程终端会话，并在其中执行命令python manage.py migrate
>
> 然后访问在线项目，确认期望看到的修改已生效

##### 7、设置 SECRET_KEY

> Django根据settings.py中SECRET_KEY设置的值来实现大量的安全协议
>
> 这个项目中提交到仓库的设置文件包含设置SECRET_KEY
>
> 对于一个练习项目而言，这足够了，但对于生产网站，应更细致地处理设置SECRET_KEY
>
> 如果项目的用途很重要，务必研究如何更安全地处理设置SECRET_KEY