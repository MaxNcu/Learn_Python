# Generated by Django 2.1.10 on 2019-07-14 00:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190714_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='open_port',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]