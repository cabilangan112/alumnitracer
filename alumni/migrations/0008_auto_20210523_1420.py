# Generated by Django 3.1.4 on 2021-05-23 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0007_remove_personalinformation_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinformation',
            name='email',
        ),
        migrations.RemoveField(
            model_name='personalinformation',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='personalinformation',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='personalinformation',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='personalinformation',
            name='user',
        ),
    ]
