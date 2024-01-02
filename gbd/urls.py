from django.contrib import admin
from django.urls import re_path
from django.urls import path
from . import views
from .views import register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
#    path('login',views.login,name='login'),
    path('GOAL',views.GOAL,name='GOAL'),
    path('register',views.register,name='register'),
#    path('register2',register2.as_view(),name='register2'),
    path('GOAL2',views.GOAL2,name='GOAL2'),
    path('GOAL3',views.GOAL3,name='GOAL3'),
    path('GOAL4',views.GOAL4,name='GOAL4'),
    path('CPA',views.CPA,name='CPA'),
    path('CPA2',views.CPA2,name='CPA2'),
    path('CPA3',views.CPA3,name='CPA3'),
    path('sample',views.sample,name='sample'),
    path('homeA',views.homeA,name='homeA'),
    path('homeB',views.homeB,name='homeB'),
    path('test',views.test,name='test'),
    path('edit/<int:num>',views.edit,name='edit'),
    path('editCPA/<int:num>',views.editCPA,name='editCPA'),
    path('editCPA2/<str:name>',views.editCPA2,name='editCPA2'),
    path('edit2/<int:num>',views.edit2,name='edit2'),
]

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)