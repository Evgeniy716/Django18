from django.contrib import admin
from django.urls import path
from task2.views import *
from task4.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func_view/',task2_func_view),
    path('class_view/', ViewByClass.as_view()),
    path('platform/', game_platform),
    path('platform/games/', game),
    path('platform/cart/', cart)
]
