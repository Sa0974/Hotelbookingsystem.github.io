from django.contrib.auth.models import User
from django.db import models

from hotel.models.room import Room


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('canceled', 'Canceled')
    ))

    def __str__(self):
        return f"{self.user.username} - {self.room.room_number}"

