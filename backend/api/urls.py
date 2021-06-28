# -*- coding: utf-8 -*-
from django.urls import path

from .views import (
    TurnOnBulb,
    TurnOffBulb,
    change_brightness,
    DiscoverBulbs,
    )

urlpatterns = [
    path('apagar/<str:bulb>', TurnOffBulb),
    path('encender/<str:bulb>', TurnOnBulb),

    path('brillo/<str:bulb>/<int:brightness>', change_brightness),

    path('buscar-luces', DiscoverBulbs),
]