# Generated by Django 2.0.5 on 2018-05-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_commodity_context'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254, verbose_name='email')),
                ('passwd1', models.CharField(max_length=255, verbose_name='passwd1')),
                ('passwd2', models.CharField(max_length=255, verbose_name='passwd2')),
                ('nick', models.CharField(max_length=255, verbose_name='nick')),
            ],
            options={
                'verbose_name': '注册用户',
            },
        ),
        migrations.AlterField(
            model_name='commodity',
            name='img',
            field=models.ImageField(upload_to='imgs/', verbose_name='商品图片'),
        ),
    ]