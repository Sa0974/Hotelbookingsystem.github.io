from django.contrib import admin

from .models.frontendslider import FrontendSlider
from .models.hotels import Hotel
from .models.room import Room
from .models.roomtype import RoomType
from .models.booking import Booking
from .models.userbooking import UserBooking
from .models.contact import ContactMessage
from .models.card_details import Card_details
from .models.slider import Slider

class AdminRoom(admin.ModelAdmin):
    list_display = ['room_number', 'room_type', 'availability']


class AdminFrontendSlider(admin.ModelAdmin):
    list_display = ['image', 'caption', 'link']


class AdminHotels(admin.ModelAdmin):
    list_display = ['name', 'address', 'description', 'amenities', 'rating']


class AdminRoomtype(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'maximum_occupancy']

class AdminBooking(admin.ModelAdmin):
    list_display = ['num_adults', 'num_childrens', 'num_rooms', 'display_total_price']

    def display_total_price(self, obj):
        return obj.total_price

    display_total_price.short_description = 'Total Price'

class UserBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'check_in', 'check_out', 'num_adults', 'num_childrens', 'num_rooms', 'status')

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message')

class Card_detailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

class SliderAdmin(admin.ModelAdmin):
    list_display = ('image','caption') 

# Register your models here.
admin.site.register(Room, AdminRoom)
admin.site.register(FrontendSlider, AdminFrontendSlider)
admin.site.register(Hotel, AdminHotels)
admin.site.register(RoomType, AdminRoomtype)
admin.site.register(Booking, AdminBooking)
admin.site.register(UserBooking, UserBookingAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Card_details, Card_detailsAdmin)

# Register your models here.
