"""为应用程序yj_logs定义URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$',views.index,name='index'),    #参数name指定这个URL模式的名字以便调用

    # 显示所有主题
    url(r'^topics/$',views.topics,name='topics'),

    # 显示特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),

    # 用于添加新主题的网页
    url(r'^new_topic/$',views.new_topic,name='new_topic'),

    # 用于添加新文章的网页
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,
        name='new_entry'),

    # 用于编辑文章的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,
        name='edit_entry'),
]