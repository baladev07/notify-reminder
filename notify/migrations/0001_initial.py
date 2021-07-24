# Generated by Django 3.2.5 on 2021-07-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reminderdetails',
            fields=[
                ('reminderid', models.BigAutoField(primary_key=True, serialize=False)),
                ('remindersub', models.CharField(max_length=200)),
                ('reminderbody', models.CharField(max_length=2000)),
                ('createdTime', models.BigIntegerField(null=True)),
                ('updatedTime', models.BigIntegerField(null=True)),
                ('remindOn', models.CharField(default=0, max_length=200)),
                ('userid', models.IntegerField(default=0)),
                ('taskid', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('username', models.CharField(max_length=100)),
                ('userid', models.BigAutoField(primary_key=True, serialize=False)),
                ('createdTime', models.BigIntegerField(null=True)),
                ('updatedTime', models.BigIntegerField(null=True)),
                ('useremail', models.EmailField(default=None, max_length=254)),
            ],
        ),
    ]