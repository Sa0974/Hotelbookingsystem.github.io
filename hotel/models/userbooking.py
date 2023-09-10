from django.db import models

class UserBooking(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    num_adults = models.IntegerField()
    num_childrens = models.IntegerField()
    num_rooms = models.IntegerField()
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Booking {self.id}"