from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='generator-index'),
    path('getdata/', views.index, name='generator-index'),
    path('about/', views.about, name='generator-about'),
    path('cisco_legacy/', views.cisco_legacy, name='generator-cisco-legacy'),
]