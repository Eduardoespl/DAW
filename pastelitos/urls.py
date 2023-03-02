from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', landing, name="landing"),
    path('post_pastel/', post_pastel, name="post_pastel"),
    path('detalle_pastel/<int:id>', updatepastel, name="updatepastel"),
    path('postm_pastel/<int:id>', updatepastel, name="postm_pastel"),
]
