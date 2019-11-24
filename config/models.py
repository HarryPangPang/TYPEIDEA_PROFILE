from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Link(models.Model):
    STATUS_NORMAl = 1
    STATUS_DELETE = 0
    STATUS_ITEM = (
        (STATUS_DELETE, "删除"),
        (STATUS_NORMAl, "正常")
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    href = models.URLField(verbose_name='链接')
    status = models.PositiveIntegerField(default=STATUS_NORMAl, choices=STATUS_ITEM, verbose_name='状态')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name='权重',
                                         help_text='权重高展示顺序靠前')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '友链'
        ordering = ['-id']


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEM = (
        (STATUS_SHOW, "显示"),
        (STATUS_HIDE, "隐藏")
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    display_type = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEM, verbose_name='展示类型')
    content = models.TextField(verbose_name='正文', help_text='如果设置的不是HTML类型，可为空')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEM, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'
