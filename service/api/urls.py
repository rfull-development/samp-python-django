# Copyright (c) 2023 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
