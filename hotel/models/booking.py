from django.db import models
from django.contrib.auth.models import User
from .room import models, Room


from django.db import models

class Booking(models.Model):
    num_adults = models.IntegerField()
    num_childrens = models.IntegerField()
    num_rooms = models.IntegerField()

    @property
    def total_price(self):
        room_price = 200  # Price per room
        return room_price * self.num_rooms

    