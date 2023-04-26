from django.contrib import admin
from django.urls import path,include
from custom import views
urlpatterns = [
    path('',views.index1),
]
