# forms.py

```python
from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):						# ①
    """根据Topic模型创建一个表单"""
    class Meta:
        model = Topic									# ②
        fields = ['text']								# ③
        labels = {'text':''}							# ④
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}										# 5
        widgets = {'text':forms.Textarea(attrs={'cols':100})}		# 6
```

> 首先导入模块forms以及要使用的模型Topic
>
> ①处——定义一个名为TopicForm的类，它继承forms.ModelForm
>
> 最简单的ModelForm版本只包含一个内嵌的Meta类
>
> 它告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段
>
> ②处——根据模型Topic创建一个表单
>
> > ③处——该表单只包含字段text
> >
> > ④处——不要为字段text生成标签
>
> 5处——字段'text'指定一个空标签
>
> 6处——定义了属性widget（小部件）
>
> > 是一个HTML表单元素，如单行文本框、多行文本区域或下拉列表
> >
> > 通过设置属性widgets，可覆盖Django选择的默认小部件
> >
> > forms.Textarea定制了字段'text'的输入小部件，将文本区域的宽度设置为100列，而不是默认的40列