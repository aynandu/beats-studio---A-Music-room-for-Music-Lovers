from django.urls import path
from .views import index

urlpatterns = [
    path('',index,name='index'),
    path('join/',index),
    path('join/1',index),
    path('create/',index),
]