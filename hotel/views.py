
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.shortcuts import redirect
from .models.room import Room
from .models.hotels import Hotel
from .models.roomtype import RoomType
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models.booking import Booking
from .models.userbooking import UserBooking
from .models.contact import ContactMessage
from .models.card_details import Card_details
from .models.slider import Slider



from datetime import datetime

def Index(request):
    hotels = Hotel.objects.all()
    bookings = Booking.objects.all()
    card_details = Card_details.objects.all()
    slider = Slider.objects.all()
    # Retrieve the user details
    user = request.user
    username = user.username
    email = user.email if user.is_authenticated else ''
    if request.method == 'POST':
        # Retrieve the submitted form data
        new_username = request.POST.get('new_username')
        new_password = request.POST.get('new_password')
        # Update the user's profile
        user.username = new_username
        if new_password:
            user.set_password(new_password)
        user.save()
        # Optionally, you can redirect the user to a success page or refresh the index page
        return redirect('index')
    context = {
        'hotels': hotels,
        'bookings': bookings,
        'card_details': card_details,
        'slider': slider,
        'username': username,
        'email': email
    }
    return render(request, 'index.html', context)

# def HomePage(request):
#     return render(request, 'index.html')
def About(request):
    return render(request, 'about.html')

def Room(request):
    return render(request, 'room.html')




def Room2(request):
    return render(request, 'room2.html')

def Room3(request):
    return render(request, 'room3.html')

def Room_details(request):
    return render(request, 'room-details.html')

def Restaurant(request):
    return render(request, 'restaurant.html')

def Spa(request):
    return render(request, 'spa.html')

def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contact_message = ContactMessage(name=name, email=email, phone=phone, subject=subject, message=message)
        contact_message.save()

        # Optionally, you can display a success message or redirect to another page
        return redirect('contact')

    return render(request, 'contact.html')

# def Booking(request):
#     return render(request, 'booking.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Your password and confirm password do not match.")
            return redirect('signup')

        # Validate other form fields here
        # Example: You can check if the username or email already exists

        try:
            User.objects.get(username=uname)
            messages.error(request, "Username already exists. Please choose a different username.")
            return redirect('signup')
        except User.DoesNotExist:
            pass

        try:
            User.objects.get(email=email)
            messages.error(request, "Email already exists. Please use a different email address.")
            return redirect('signup')
        except User.DoesNotExist:
            pass

        # If all validations pass, create the user
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()

        messages.success(request, "Your account has been created successfully. You can now log in.")
        return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,'User name and password is incorrect.')

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')



def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Handle the case where the email does not exist in the database
            # Display an appropriate error message to the user
            return render(request, 'forgot.html')

        # Generate a password reset token
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)

        # Send a password reset email to the user
        reset_url = request.build_absolute_uri(reverse('reset_password', kwargs={'uid': user.pk, 'token': token}))
        subject = 'Password Reset'
        message = f'Click the following link to reset your password: {reset_url}'
        send_mail(subject, message, 'your_email@example.com', [email])

        # Redirect the user to a confirmation page
        return redirect('password_reset_sent')

    return render(request, 'forgot.html')


def reset_password(request, uid, token):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Handle password reset logic, validate passwords, and reset the password

        # Redirect the user to a success page or handle any errors

    return render(request, 'reset_password.html', {'uid': uid, 'token': token})

# def profile_view(request):
#     # Retrieve the user details
#     user = request.user
#     username = user.username
#     email = user.email

#     context = {
#         'username': username,
#         'email': email
#     }

#     return render(request, 'profile.html', context)

# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         new_username = request.POST.get('new_username')
#         new_email = request.POST.get('new_email')

#         # Update the user's profile with the new details
#         user = request.user
#         user.username = new_username
#         user.email = new_email
#         user.save()

#         return redirect('profile')  # Redirect back to the profile page

#     return redirect('profile')  

@login_required
def user_data(request):
    # Retrieve the user details
    user = request.user
    username = user.username
    email = user.email

    # Return the user data as JSON
    data = {
        'username': username,
        'email': email
    }

    return JsonResponse(data)

def Mybooking(request):
    booking = UserBooking.objects.first()

    if booking is None:
        # Create a new UserBooking object if none exists
        booking = UserBooking()

    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        num_adults = request.POST.get('num_adults')
        num_childrens = request.POST.get('num_childrens')
        num_rooms = request.POST.get('num_rooms')

        # Convert date strings to datetime objects with the correct format
        try:
            check_in = datetime.strptime(check_in, '%m/%d/%Y').strftime('%Y-%m-%d')
            check_out = datetime.strptime(check_out, '%m/%d/%Y').strftime('%Y-%m-%d')
        except ValueError:
            # Handle invalid date format error
            return render(request, 'error.html')

        # Update the existing UserBooking instance with the new values
        booking.check_in = check_in
        booking.check_out = check_out
        booking.num_adults = num_adults
        booking.num_childrens = num_childrens
        booking.num_rooms = num_rooms

        # Save the instance to the database
        booking.save()

        # Return a response, such as rendering a template or redirecting to another page
        return redirect('mybooking')  # Redirect to the same page to display the updated booking
    else:
        # Handle GET requests or other cases
        return render(request, 'mybooking.html', {'booking': booking})
def update_status(request, booking_id):
    if request.method == 'POST':
        booking = UserBooking.objects.get(id=booking_id)
        status = request.POST.get('status')

        # Check if the chosen status is valid
        valid_statuses = [choice[0] for choice in UserBooking.STATUS_CHOICES]
        if status not in valid_statuses:
            return JsonResponse({'status': 'error', 'message': 'Invalid status'})

        # Update the status of the booking
        booking.status = status
        booking.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

