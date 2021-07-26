from django.urls import path

from . import views, run_task

urlpatterns = [
    path('user', views.userMethod),
    path('user/<str:pk>', views.updateUSer),
    path('reminder', views.addReminder),
    path('reminder/<str:pk>', views.updateReminder),
    path('users', views.usersList),
    path('start', views.start)
    # path('reminders', views.reminderList)

]
