from django.shortcuts import render
from rest_framework import generics,status
from .models import Room
from .serializers import RoomSerializer,CreateRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class RoomView(generics.CreateAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer

class CreatRoomView(APIView):
    serializer_class=CreateRoomSerializer
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            guestCanPause=serializer.data.get('guestCanPause')
            votesToSkip=serializer.data.get('votesToSkip')
            host=self.request.session.session_key
            queryset=Room.objects.filter(host=host)
        if queryset.exists():
            room=queryset[0]
            room.guestCanPause=guestCanPause
            room.votesToSkip=votesToSkip
            room.save(update_fields=['guestCanPause','votesToSkip'])
        else:
            room=Room(host=host,guestCanPause=guestCanPause,votesToSkip=votesToSkip)
            room.save()
        return Response(RoomSerializer(room).data,status=status.HTTP_201_CREATED)