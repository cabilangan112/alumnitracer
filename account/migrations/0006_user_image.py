# Generated by Django 3.1.4 on 2021-07-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210708_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.FileField(null=True, upload_to='cover'),
        ),
    ]