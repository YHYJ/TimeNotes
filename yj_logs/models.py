from django.db import models
from django.contrib.auth.models import User

# Create your models here.——定义模型。模型即类,类即数据库表

class Topic(models.Model):
    """主题"""
    text = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User)

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