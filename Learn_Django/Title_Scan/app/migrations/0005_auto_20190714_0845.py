# Generated by Django 2.1.10 on 2019-07-14 00:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_datas_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='open_port',
            field=ckeditor.fields.RichTextField(),
        ),
    ]