from django.db import models
from .roomtype import models, RoomType


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number
