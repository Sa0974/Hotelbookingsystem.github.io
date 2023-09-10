from django.contrib.auth.models import User
from django.db import models

from hotel.models.hotels import Hotel


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name}"

