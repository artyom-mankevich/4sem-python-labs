# Generated by Django 3.0.3 on 2020-04-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200408_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Лайк', 'verbose_name_plural': 'Лайки'},
        ),
        migrations.AlterField(
            model_name='like',
            name='like_or_dislike',
            field=models.BooleanField(verbose_name='Лайк'),
        ),
    ]
