from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetMembers, name='GetMembers'),
]