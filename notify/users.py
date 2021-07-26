import math
import re
from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.utils import json

from .models import userdetails
from rest_framework.response import Response

from .serializers import userdetailsSerializer


def getCurrentTimeInSec():
    return math.ceil(datetime.now().timestamp())


class user:

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        self.userMap = {}
        self.validationList = []

    def isEmpty(self):
        if not self.name:
            return Response({"message": "username is empty"}, status=400)
        if not self.email:
            return Response({"message": "user_email is empty"}, status=400)

    def isvalidName(self):
        regex = re.compile('[#$%^&()?/":;\|]')
        if regex.search(self.name) is not None:
            return Response({"message": "Special characters are not allowed"}, status=400)

    def toLower(self):
        return self.name.lower()

    def isValidMail(self, email):
        if '@gmail.com' not in (self.email or email):
            return Response({"message": "please enter valid email_id"}, status=400)

    def isDuplicateName(self):
        try:
            userObject = userdetails.objects.get(username=self.name)
            return Response({"message": "username already exists"}, status=400)
        except userdetails.DoesNotExist:
            pass

    def isDuplicateEmail(self):
        try:
            userObject = userdetails.objects.get(useremail=self.email)
            return Response({"message": "user_email already exists"}, status=400)
        except userdetails.DoesNotExist:
            pass

    def userMapping(self):
        self.userMap['username'] = self.name
        self.userMap['useremail'] = self.email
        return self.userMap

    def userValidation(self):
        self.validationList.append(self.isEmpty())
        self.validationList.append(self.isvalidName())
        self.validationList.append(self.isValidMail("@gmail.com"))
        self.validationList.append(self.isDuplicateName())
        self.validationList.append(self.isDuplicateEmail())
        for res in self.validationList:
            if res is not None:
                return res


def getUserDetail(username):
    try:
        userMap = {}
        dataObject = userdetails.objects.get(username=username)
        userMap['useremail'] = dataObject.useremail
        userMap['userid'] = dataObject.userid
        return userMap
    except userdetails.DoesNotExist:
        raise APIException("user does not exists.", 500)


def isValid(username):
    user_detail = getUserDetail(username)
    if not user_detail:
        return False
    return True


def deleteUser(user_id):
    userObject = userdetails.objects.get(userid=user_id)
    userObject.delete()
    return Response({"Message": "User has been deleted"}, status=200)


def createUser(user_map):
    user_map['created_time'] = getCurrentTimeInSec()
    user_map['updated_time'] = getCurrentTimeInSec()
    serializedRes = userdetailsSerializer(data=user_map)
    if serializedRes.is_valid():
        serializedRes.save()
        return Response({"message": "User added successfully"}, status=201)
    return Response({"message": "internal error"}, status=500)


def getUsersList(users=[]):
    try:
        userObject = userdetails.objects.all()
        serializerRes = userdetailsSerializer(userObject, many=True)
        # users.append(serializerRes.data)
        return serializerRes.data
    except Exception as e:
        raise APIException(e, 500)


def updateUser(user_map, user_id):
    user_map['updated_time'] = getCurrentTimeInSec()
    user_obj = userdetails.objects.get(userid=user_id)
    serializedRes = userdetailsSerializer(instance=user_obj, data=user_map)
    if serializedRes.is_valid():
        serializedRes.save()
        return Response({"message": "User updated successfully"}, status=201)
    return Response({"message": "internal error"}, status=500)


def getUser(user_id, user_map={}):
    try:
        dataObject = userdetails.objects.get(userid=user_id)
        user_map['user_email'] = dataObject.useremail
        user_map['user_name'] = dataObject.username
        user_map['user_id'] = dataObject.userid
        return user_map
    except userdetails.DoesNotExist:
        raise APIException("user does not exists.", 400)
