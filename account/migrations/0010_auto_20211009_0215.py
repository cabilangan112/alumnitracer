# Generated by Django 3.2.6 on 2021-10-09 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
