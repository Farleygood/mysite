
# coding:utf-8
from django.db import models

# Create your models her.

from django.db import models

class User(models.Model):

    gender = (
        ('mail', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"          # 给模型起一个名字
        verbose_name_plural = "用户"   # 模型的复数形式