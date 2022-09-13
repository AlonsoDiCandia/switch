# -*- coding: utf-8 -*-
from django.urls import path

from .views.bulbs.views import (
    TurnOnOffBulb,
    TurnOnAllBulbs
    )

urlpatterns = [
    path('power/all', TurnOnAllBulbs),
    path('power/<str:bulb>', TurnOnOffBulb),

    # path('brillo/<str:bulb>/<int:brightness>', change_brightness),
]