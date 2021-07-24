from django.db import models
from django.utils import timezone


class userdetails(models.Model):
    username = models.CharField(max_length=100)
    userid = models.BigAutoField(primary_key=True)
    created_time = models.BigIntegerField(null=True, default=0)
    updated_time = models.BigIntegerField(null=True, default=0)
    useremail = models.EmailField(default=None)

    def __str__(self):
        return str(self.userid)

    def __str__(self):
        return str(self.username)


class reminderdetails(models.Model):
    reminderid = models.BigAutoField(primary_key=True)
    remindersub = models.CharField(max_length=200)
    reminderbody = models.CharField(max_length=2000)
    created_time = models.BigIntegerField(null=True)
    updated_time = models.BigIntegerField(null=True)
    remindOn = models.CharField(max_length=200, default=0)
    userid = models.IntegerField(default=0)
    taskid = models.IntegerField(default=0)
    username = models.CharField(max_length=50, null=True)
    reminderStatus = models.CharField(null=False, default='Yet to remind', max_length=20)
