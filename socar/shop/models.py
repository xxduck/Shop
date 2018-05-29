from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Commodity(models.Model):
    #  商品详情
    STATUS = (
        (1, "在售"),
        (2, "缺货"),
        (3, "下架"),
    )
    name = models.CharField(verbose_name='商品名称', max_length=255)
    price = models.FloatField(verbose_name="商品价格")
    discount = models.FloatField(verbose_name="商品折扣")
    status = models.IntegerField(verbose_name="商品状态", choices=STATUS)
    ptime = models.DateTimeField("上架时间", auto_now=True)
    context = RichTextUploadingField(null=True)
    img = models.ImageField(verbose_name="商品图片", upload_to='imgs/')

    class Meta:
        verbose_name = verbose_name_plural = "商品信息"


class MyUser(models.Model):
    # 用户模型

    username = models.EmailField(verbose_name="email")
    passwd1 = models.CharField(verbose_name="passwd1", max_length=255, null=False)
    passwd2 = models.CharField(verbose_name="passwd2", max_length=255)
    nick = models.CharField(verbose_name="nick", max_length=255)
    create_time =  models.DateTimeField(verbose_name="注册时间", auto_now=True)
    last_login = models.DateTimeField(verbose_name="上次登录时间", auto_now=True)

    class Meta:
        verbose_name = "注册用户"