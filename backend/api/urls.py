# -*- coding: utf-8 -*-
from django.urls import path

from .views import (
    TurnOnBulb,
    TurnOffBulb
    )

urlpatterns = [
    path('apagar/<str:bulb>', TurnOffBulb),
    path('encender/<str:bulb>', TurnOnBulb),
]