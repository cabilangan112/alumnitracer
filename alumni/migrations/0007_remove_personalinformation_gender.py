# Generated by Django 3.1.4 on 2021-05-21 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0006_auto_20210521_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinformation',
            name='gender',
        ),
    ]
