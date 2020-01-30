from django.urls import path
from siteapp.views import *



app_name = 'siteapp'

urlpatterns = [
    path('',  index, name='index'),
]
