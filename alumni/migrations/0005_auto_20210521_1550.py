# Generated by Django 3.1.4 on 2021-05-21 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0004_auto_20210521_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parallax',
            name='user',
        ),
        migrations.RemoveField(
            model_name='thumbnail',
            name='user',
        ),
        migrations.DeleteModel(
            name='Index',
        ),
        migrations.DeleteModel(
            name='Parallax',
        ),
        migrations.DeleteModel(
            name='Thumbnail',
        ),
    ]