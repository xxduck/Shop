# Generated by Django 2.0.5 on 2018-05-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180521_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='ptime',
            field=models.DateTimeField(auto_now=True, verbose_name='上架时间'),
        ),
    ]
