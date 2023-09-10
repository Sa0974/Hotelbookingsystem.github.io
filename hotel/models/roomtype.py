from django.db import models

class RoomType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    maximum_occupancy = models.PositiveIntegerField()

    def __str__(self):
        return self.name

