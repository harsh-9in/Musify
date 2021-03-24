from django.shortcuts import render
from .models import Room
from .serializers import RoomSerializer
from rest_framework import viewsets
# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class=RoomSerializer
    queryset=Room.objects.all()


