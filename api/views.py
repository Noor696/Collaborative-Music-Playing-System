from django.shortcuts import render
from rest_framework import generics  # this allows to make class inhiret from API view
from .models import Room
from .serializers import RoomSerializer
# Create your views here.

class RoomView(generics.ListAPIView):
    # Allow us to view all the different model (Rooms) and Create A Room
    queryset = Room.objects.all() # tell the queryset what do we want to return / take all of room object and give him to serilizer
    serializer_class = RoomSerializer  # a file resposible to convert python code to JSON data/ format
