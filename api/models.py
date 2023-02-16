from django.db import models

# Create your models here.

# room Model -> group similar users together, that room will have control over the host music, one person hosting or playing music and then other people join to this room, and while they can control that music

class Room(models.Model):

      
      code = models.CharField(max_length=25, default="", unique=True)
      host = models.CharField(max_length=50, unique=True) # one host for one room
      guest_can_pause = models.BooleanField(null=False, default=False)
      votes_to_skip = models.IntegerField(null=False, default=1)
      created_at = models.DateTimeField(auto_now_add=True)
      


      # code : is going to be a unique code that identifies the rooms / unique=True : one code for one room
      # guest_can_pause : this permission , is the guest allowed to pause the music or play 