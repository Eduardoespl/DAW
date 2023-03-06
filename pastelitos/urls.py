from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from pastelitos.views import *
from .views import *
from . import views

urlpatterns = [
    url(r'^$',landing, name="landing"),
    path('post_pastel/',post_pastel,name="post_pastel"),
    path('detalle_pastel/<int:id>', updatepastel,name="updatepastel"),
    path('datos_modal/<int:id>', updatepastel,name="postm_pastel"),
    path('datos_modal/<int:id>/', views.datos_modal, name='datos_modal'),
]