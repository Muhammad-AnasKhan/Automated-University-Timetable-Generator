from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('login/', CustomLoginView.as_view(), name='login'), # custom login view
    path("timetableGeneration/", timetable, name="timetable"),
    path("testSplit/", testSplit, name="testSplit"),
    path("instructorAdd/", instructorAdd, name="instructorAdd"),
    path("instructorEdit/", instructorEdit, name="instructorEdit"),
    path("instructorDelete/<int:pk>/", instructorDelete, name="deleteinstructor"),
    path("roomAdd/", roomAdd, name="roomAdd"),
    path("roomEdit/", roomEdit, name="roomEdit"),
    path("roomDelete/<int:pk>/", roomDelete, name="deleteroom"),
    path("meetingTimeAdd/", meetingTimeAdd, name="meetingTimeAdd"),
    path("meetingTimeEdit/", meetingTimeEdit, name="meetingTimeEdit"),
    path("meetingTimeDelete/<str:pk>/", meetingTimeDelete, name="deletemeetingtime"),
    path("courseAdd/", courseAdd, name="courseAdd"),
    path("courseEdit/", courseEdit, name="courseEdit"),
    path("courseDelete/<str:pk>/", courseDelete, name="deletecourse"),
    path("departmentAdd/", departmentAdd, name="departmentAdd"),
    path("departmentEdit/", departmentEdit, name="departmentEdit"),
    path("departmentDelete/<int:pk>/", departmentDelete, name="deletedepartment"),
    path("sectionAdd/", sectionAdd, name="sectionAdd"),
    path("sectionEdit/", sectionEdit, name="sectionEdit"),
    path("sectionDelete/<str:pk>/", sectionDelete, name="deletesection"),
    path("api/genNum/", apiGenNum, name="apiGenNum"),
    path("api/terminateGens/", apiterminateGens, name="apiterminateGens"),

    # teacher-preference module starts 
    path('teacher-preference/', teacher_preference_view, name='teacher_preference'),
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('save_teacher_preference/', save_teacher_preference, name='save_teacher_preference'),
    path('generate_teacher_preferenced_timetable/', generate_teacher_preferenced_timetable, name='generate_teacher_preferenced_timetable'),
    path('teacher-preference/success/', teacher_preference_success, name='teacher_preference_success'),
    path('load-courses/', load_courses, name='load_courses'),
    path('get-timeslots/', get_timeslots, name='get_timeslots'),

    # users module
    path('users/', manage_users, name='manageUsers')
]
