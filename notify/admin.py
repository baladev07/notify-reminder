from django.contrib import admin
from .models import userdetails, reminderdetails


class notifyAdmin(admin.ModelAdmin):
    list_display = ('username', 'userid', 'useremail', 'created_time', 'updated_time')


class reminderAdmin(admin.ModelAdmin):
    list_display = ('reminderid', 'remindersub', 'reminderbody', 'remindOn', 'username', 'created_time', 'updated_time',
                    'reminderStatus')


admin.site.register(userdetails, notifyAdmin)

admin.site.register(reminderdetails, reminderAdmin)
