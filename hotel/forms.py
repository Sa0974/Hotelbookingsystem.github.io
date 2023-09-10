from django import forms
from .models.userbooking import UserBooking


class UserBookingForm(forms.ModelForm):
    class Meta:
        model = UserBooking
        fields = ['check_in', 'check_out', 'num_adults', 'num_childrens', 'num_rooms']
