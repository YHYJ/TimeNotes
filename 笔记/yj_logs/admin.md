# admin.py

```python
from django.contrib import admin

from yj_logs.models import Topic,Entry	##导入要注册的模型Topic

admin.site.register(Topic)			##使用admin.site.register()让Django通过管理网站管理模型
admin.site.register(Entry)
```

