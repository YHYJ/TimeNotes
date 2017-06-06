from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.——创建yj_logs的视图函数

from .models import Topic,Entry
from .forms import TopicForm,EntryForm

def index(request):
    """主页"""
    return render(request,'yj_logs/index.html')

@login_required()
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'yj_logs/topics.html',context)

@login_required()
def topic(request,topic_id):
    """显示特定主题及其所有文章"""
    topic = get_object_or_404(Topic,id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'yj_logs/topic.html',context)

@login_required()
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # GET——未提交数据，创建一个新表单
        form = TopicForm()
    else:
        # POST——提交了数据，对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('yj_logs:topics'))

    context = {'form':form}
    return render(request,'yj_logs/new_topic.html',context)

@login_required()
def new_entry(request,topic_id):
    """在特定的主题中添加新文章"""
    topic = get_object_or_404(Topic,id=topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # GET——未提交数据，创建一个新表单
        form = EntryForm()
    else:
        # POST——提交了数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('yj_logs:topic',
                                                args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,'yj_logs/new_entry.html',context)

@login_required()
def edit_entry(request,entry_id):
    """编辑既有文章"""
    entry = get_object_or_404(Entry,id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求，使用当前文章填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的请求，对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('yj_logs:topic',
                                                args=[topic.id]))

    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'yj_logs/edit_entry.html',context)