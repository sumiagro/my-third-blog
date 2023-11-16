from django.contrib import admin
from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('GOAL',views.GOAL,name='GOAL'),
    path('GOAL2/<str:name>',views.GOAL2,name='GOAL2'),
    path('GOAL3',views.GOAL3,name='GOAL3'),
    path('GOAL4/<str:name>',views.GOAL4,name='GOAL4'),
    path('CPA',views.CPA,name='CPA'),
    path('CPA2/<str:name>',views.CPA2,name='CPA2'),
    path('CPA3/<str:name>',views.CPA3,name='CPA3'),
    path('sample',views.sample,name='sample'),
    path('homeA',views.homeA,name='homeA'),
    path('homeB',views.homeB,name='homeB'),
    path('test',views.test,name='test'),
    path('edit/<int:num>',views.edit,name='edit'),
    path('editCPA/<int:num>',views.editCPA,name='editCPA'),
    path('editCPA2/<str:name>',views.editCPA2,name='editCPA2'),
    path('edit2/<str:name>',views.edit2,name='edit2'),
]
