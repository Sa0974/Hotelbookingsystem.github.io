from django.conf import settings

from django.conf.urls.static import static
from django.urls import path

from .import views
from .views import Mybooking

urlpatterns = [
     path('', views.Index, name='index'),
     path('about', views.About),
     path('room', views.Room),
     path('room2', views.Room2),
     path('room3', views.Room3),
     path('room-details', views.Room_details),
     path('restaurant', views.Restaurant),
     path('spa', views.Spa),
     path('contact', views.Contact),
     path('booking', views.Booking),
     path('contact', views.Contact, name='contact'),
     path('login', views.LoginPage, name='login'),
     path('signup', views.SignupPage, name='signup'),
     path('logout', views.LogoutPage, name='logout'),
     path('forgot_password', views.forgot_password, name='forgot_password'),
     path('reset_password<int:uid>/<str:token>', views.reset_password, name='reset_password'),
     path('user-data/', views.user_data, name='user_data'),
     path('mybooking', Mybooking, name='mybooking'),
     path('bookings/update_status/<int:booking_id>/', views.update_status, name='update_status'),
   



              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
