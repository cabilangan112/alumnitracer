# Generated by Django 3.1.4 on 2021-05-21 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0003_auto_20210521_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
        migrations.RemoveField(
            model_name='department',
            name='user',
        ),
    ]