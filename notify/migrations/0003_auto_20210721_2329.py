# Generated by Django 3.2.5 on 2021-07-21 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0002_auto_20210721_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminderdetails',
            name='createdTime',
        ),
        migrations.RemoveField(
            model_name='reminderdetails',
            name='updatedTime',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='createdTime',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='updatedTime',
        ),
    ]