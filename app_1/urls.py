from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("register", views.register, name="register"),
    path('accounts/', include('accounts.urls')),
    path('', views.index, name='index'),
]