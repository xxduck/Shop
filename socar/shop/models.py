from django.db import models

# Create your models here.


class Commodity(models.Model):
    #  商品
    STATUS = (
        (1, "在售"),
        (2, "缺货"),
        (3, "下架"),
    )
    name = models.CharField(verbose_name='商品名称', max_length=255)
    price = models.FloatField(verbose_name="商品价格")
    status = models.IntegerField(verbose_name="商品状态", choices=STATUS)
    ptime = models.DateTimeField("上架时间", auto_now=True)

    class Meta:
        verbose_name = verbose_name_plural = "商品信息"