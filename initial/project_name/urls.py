from django.urls import include
from django.urls import path

from .views import *

urlpatterns = [
    path('home', {{ camel_case_project_name }}View.as_view(), name='home'),
    path('index', {{ camel_case_project_name }}View.as_view(), name='home'),
    path('', {{ camel_case_project_name }}View.as_view(), name='home'),
]
