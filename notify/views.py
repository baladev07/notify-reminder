from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import users, reminderUtils
from rest_framework.exceptions import APIException


@api_view(['POST', 'GET', 'DELETE'])
def userMethod(request):
    try:
        user = users.user()
        username = request.data['username']
        if request.method == 'POST':
            user.name = username
            user.email = request.data['user_email']
            userValidation = user.userValidation()
            if not userValidation:
                return users.createUser(user.userMapping())
            else:
                return userValidation
        if request.method == "GET":
            return Response(users.getUserDetail(username), status=200)

    except Exception as e:
        raise APIException(e, 500)


@api_view(['POST', 'GET'])
def addReminder(request):
    reminder = reminderUtils.reminder()
    username = request.query_params['username']
    if users.isValid(username):
        if request.method == 'POST':
            reminder.username = username
            reminder.reminderDate = request.data['remindondate']
            reminder.reminderTime = request.data['remindontime']
            reminder.remindTo = request.data['remindto']
            reminder.reminderSub = request.data['remindersub']
            reminder.reminderBody = request.data['reminderbody']
            reminder_validation = reminder.reminderValidation()
            if not reminder_validation:
                try:
                    isCreated = reminderUtils.createReminder(reminder.reminderMapping(), request)
                except Exception as e:
                    raise APIException(e, 500)
                return Response(isCreated, status=201)
            else:
                return reminder_validation
        if request.method == 'GET':
            return Response(reminderUtils.getUserReminderDetails(username), status=200)
    else:
        return Response({'message': "user does not exists"}, status=400)


@api_view(['PUT', 'DELETE', 'GET'])
def updateReminder(request, pk):
    reminder = reminderUtils.reminder()
    if request.method == "PUT":
        username = request.query_params['username']
        reminder.reminderDate = request.data['remindondate']
        reminder.reminderTime = request.data['remindontime']
        reminder.reminderSub = request.data['remindersub']
        reminder.reminderBody = request.data['reminderbody']
        reminder.remindTo = request.data['remindto']
        reminderValidation = reminder.reminderValidation()
        if not reminderValidation:
            try:
                isUpdated = reminderUtils.updateReminder(reminder.reminderMapping(), username, pk, request)
            except Exception as e:
                raise APIException(e, 500)
            return isUpdated
        else:
            return reminderValidation

    if request.method == "DELETE":
        return Response(reminderUtils.deleteReminder(pk), 200)

    if request.method == 'GET':
        # userid = request.query_params['userid']
        reminder_details = reminderUtils.getReminder(pk)
        return Response({"result": reminder_details}, status=200)


@api_view(['PUT', 'GET', 'DELETE'])
def updateUSer(request, pk):
    try:
        user = users.user()
        if request.method == 'PUT':
            user.name = request.data['username']
            user.email = request.data['user_email']
            return users.updateUser(user.userMapping(), pk)
        if request.method == 'GET':
            return Response({'result': users.getUser(pk)})
        if request.method == "DELETE":
            return users.deleteUser(pk)
    except Exception as e:
        raise APIException(e, 500)


@api_view(['GET'])
def usersList(request):
    return Response({'user': users.getUsersList()}, status=200)
