from django.urls import path
from . import views
from django.contrib import admin

app_name = 'mamozon'

urlpatterns = [
    path('lp/', views.Lp.as_view(), name='lp'),
]
