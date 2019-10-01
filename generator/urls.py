from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='generator-index'),
    path('viptela/', views.viptela, name='generator-viptela'),
    path('adva/', views.adva, name='generator-adva'),
    path('cisco_legacy/', views.cisco_legacy, name='generator-cisco-legacy'),
    path('getdata/', views.index, name='generator-index'),
    path('about/', views.about, name='generator-about'),
]