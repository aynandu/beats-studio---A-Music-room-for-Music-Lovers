from django.urls import path
from  .views import RoomView,CreatRoomView
urlpatterns = [
    path('',RoomView.as_view(),name="roomView"),
    path('created/',CreatRoomView.as_view())
]
