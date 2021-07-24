import math
from datetime import datetime
from hashlib import sha1

from django.utils import timezone
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.utils import json

from background_task.models import Task
from notify.serializers import reminderdetailsSerializer, backgroundSerializer

from . import users, mail
from .models import reminderdetails


class reminder:

    def __init__(self, reminder_sub=None, reminder_body=None, remind_to=None, username=None, reminder_date=None,
                 reminder_time=None):
        self.reminderSub = reminder_sub
        self.reminderBody = reminder_body
        self.remindTo = remind_to
        self.reminderMap = {}
        self.username = username
        self.reminderDate = reminder_date
        self.reminderTime = reminder_time
        self.reminder_validation = []

    def isEmpty(self):
        if not self.reminderSub:
            return Response({"message": "Subject should not be empty"}, status=400)
        if not self.remindTo:
            return Response({"message": "Invalid user_email"}, status=400)

        # uncomment this if you need reminderBody mandatory
        # if not self.reminderBody:
        #     return Response({"message": "Subject should not be empty"}, status=400)

    def timeInDateFormat(self):
        return datetime.strptime(self.reminderDate + ' ' + self.reminderTime + ":00", '%d-%m-%Y %H:%M:%S')

    def isFutureTime(self):
        DateInSec = self.timeInDateFormat().timestamp()
        currentTimeInSec = datetime.today().timestamp()
        if DateInSec <= currentTimeInSec:
            return Response({'message': "Only future date and time are allowed"}, status=400)

    def reminderMapping(self):
        self.reminderMap['remindersub'] = self.reminderSub
        self.reminderMap['reminderbody'] = self.reminderBody
        self.reminderMap['username'] = self.username
        self.reminderMap['remindOn'] = math.ceil(self.timeInDateFormat().timestamp())
        self.reminderMap['remindTo'] = self.remindTo
        return self.reminderMap

    def reminderValidation(self):
        self.reminder_validation.append(self.isEmpty())
        self.reminder_validation.append(self.isFutureTime())
        for res in self.reminder_validation:
            if res is not None:
                return res


def createReminder(reminder_map, request):
    try:
        user_email = reminder_map.get('remindTo')
        user_name = reminder_map.get('username')
        time_in_sec = reminder_map.get('remindOn')
        reminder_map['remindOn'] = str(time_in_sec)
        reminder_map['created_time'] = users.getCurrentTimeInSec()
        reminder_map['updated_time'] = users.getCurrentTimeInSec()
        created_time = reminder_map.get('created_time')
        updated_time = reminder_map.get('updated_time')
        serializedRes = reminderdetailsSerializer(data=reminder_map)
        # mail.sendMail(reminder_map, user_email, schedule=30)
        if serializedRes.is_valid():
            serializedRes.save()
            reminder_map.pop('created_time')
            reminder_map.pop('updated_time')
            job_added = addJob(reminder_map, user_email, user_name, updated_time, created_time, request)
            if job_added:
                return {"message": "Reminder added successfully"}
    except Exception as e:
        raise APIException(e, 500)


def updateReminder(reminder_map, username, reminder_id, request):
    try:
        user_email = reminder_map.get('remindTo')
        reminder_map.pop('remindTo')
        current_time = users.getCurrentTimeInSec()
        reminder_map['updated_time'] = current_time
        reminder_map['username'] = username
        reminder_created_time = getReminder(reminder_id).get('created_time')
        reminderObject = reminderdetails.objects.get(reminderid=reminder_id)
        serializerRes = reminderdetailsSerializer(instance=reminderObject, data=reminder_map)
        if reminderObject.reminderStatus != 'completed':
            if serializerRes.is_valid():
                serializerRes.save()
                reminder_map.pop('updated_time')
                job_added = addJob(reminder_map, user_email, username, current_time, reminder_created_time, request)
                if job_added:
                    return Response({"message": "Reminder updated successfully."}, status=200)
        else:
            return Response({"message": "you cannot edit already notified reminder.please create a new reminder."}, status=400)
    except Exception as e:
        raise APIException(e, 500)


def getUserReminderDetails(username, reminders=[]):
    try:
        reminderObject = reminderdetails.objects.all().filter(username=username)
        serializerRes = reminderdetailsSerializer(instance=reminderObject, many=True)
        # reminders.append(serializerRes.data)
        return Response({"result": serializerRes.data}, status=200)
    except reminderdetails.DoesNotExist:
        return {'message': 'There are no reminders.'}


def deleteTask(created_time):
    """
    Need to add delete rmeinder method here....for now task has been deleted
    """
    try:
        task_object = Task.objects.get(createdTime=created_time)
        task_object.delete()
        return True
    except Task.DoesNotExist:
        pass


def getReminder(reminder_id):
    """
    In future have return a map.. instead of return serializer
    """
    try:
        reminderObject = reminderdetails.objects.get(reminderid=reminder_id)
        serializerRes = reminderdetailsSerializer(instance=reminderObject, many=False)
        return serializerRes.data
    except reminderdetails.DoesNotExist:
        raise APIException('Reminder does not exists.', 400)


def addJob(reminder_map, user_email, username, current_time, reminder_created_time, request):
    """
        Now using this to add only email method but in future it will  be updated..
    """
    task_name = "notify.mail.sendMail"
    List = (reminder_map, user_email)
    time_in_sec = reminder_map.get('remindOn')
    date_time = datetime.fromtimestamp(int(time_in_sec)).strftime('%Y-%m-%d %H:%M:%S')
    reminder_map.pop('remindOn')
    task_params = json.dumps((List, {}), sort_keys=True)
    s = "%s%s" % (task_name, task_params)
    task_hash = sha1(s.encode('utf-8')).hexdigest()
    data = {"task_name": task_name, "task_params": task_params, "run_at": date_time, "priority": 0,
            "username": username, "updatedTime": current_time, "createdTime": reminder_created_time,
            "task_hash": task_hash}
    if request.method == "PUT":
        taskObject = Task.objects.get(createdTime=reminder_created_time)
        serializerRes = backgroundSerializer(instance=taskObject, data=data)
    else:
        serializerRes = backgroundSerializer(data=data)
    if serializerRes.is_valid():
        serializerRes.save()
        return True


def deleteReminder(reminder_id):
    try:
        reminderObject = reminderdetails.objects.get(reminderid=reminder_id)
        created_time = reminderObject.created_time
        reminderObject.delete()
        if deleteTask(created_time):
            return {'message': "Reminder deleted successfully"}
    except reminderdetails.DoesNotExist:
        raise APIException('Reminder does not exists.', 400)
