#Importing Libraries
from django.urls import path
from . import views
#paths/ routes/ endpoints/urls/patterns

urlpatterns = [
    path('hello', views.hello )
]
