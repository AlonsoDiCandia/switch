# -*- coding: utf-8 -*-
from django.urls import path

from .views import (
    TurnOnOffBulb,
    change_brightness,
    )

urlpatterns = [
    path('power/<str:bulb>', TurnOnOffBulb),

    path('brillo/<str:bulb>/<int:brightness>', change_brightness),
]