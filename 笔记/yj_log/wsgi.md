# wsgi.py

```python
"""
WSGI config for yj_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling													# 1

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yj_log.settings")

application = Cling(get_wsgi_application())									# 2
```

> 1处——导入帮助正确地提供静态文件的Cling
>
> 2处——使用Cling来启动应用程序
>
> > 这些代码在本地也适用，因此无需将其放在if代码块内