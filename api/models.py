from django.db import models
import string , random  # we use this to generate the random code 

# Create your models here.

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # -> then check this code is unique by looking for all the rooms in our database and cheking if they have a code like this
        # filter all of room object by check the code if equal the generate code
        # use count to return to me a list of all of the objects that meet this criteria (code=code)
        if Room.objects.filter(code=code).count() == 0 :
            break

        # if not true we will keep generating more code until one it's unique 

    return code





# room Model -> group similar users together, that room will have control over the host music, one person hosting or playing music and then other people join to this room, and while they can control that music

class Room(models.Model):

      
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True) # one host for one room
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
      


    # code :(random number / eight digit) is going to be a unique code that identifies the rooms / unique=True : one code for one room
    # guest_can_pause : this permission , is the guest allowed to pause the music or play 