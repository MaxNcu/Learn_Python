# Generated by Django 2.1.10 on 2019-07-12 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190712_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datas',
            name='url',
        ),
    ]