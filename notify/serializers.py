from rest_framework import serializers
from .models import userdetails, reminderdetails

from background_task.models import Task


class userdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = userdetails
        fields = ['username', 'userid', 'useremail', 'created_time', 'updated_time']


class reminderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reminderdetails
        fields = ['remindersub', 'reminderbody', 'remindOn', 'username', 'reminderid', 'created_time', 'updated_time',
                  'reminderStatus']


class backgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_params', 'run_at', 'updatedTime', 'task_name', 'username', 'createdTime', 'priority']
