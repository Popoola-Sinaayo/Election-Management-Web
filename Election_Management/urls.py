from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("polls", view_polling_unit),
    path('store', store_result)
]
