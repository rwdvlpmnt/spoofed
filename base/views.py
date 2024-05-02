from django.shortcuts import render, redirect


def login(request):
    return render(request, 'Login.html')

def register(request):
    return render(request, 'Register.html')

def logout(request):
    return render(request, 'Logout.html')

def home(request):
    return render(request, 'Home.html')

def profile(request):
    return render(request, 'Profile.html')
# Create your views here.

def google_login(request):
    # Logic for initiating Google OAuth authentication
    return redirect('google_oauth_url')  # Redirect to Google OAuth URL

def google_oauth_view(request):
    # Your Google OAuth logic here
    return redirect('home') # Redirect to 'home' or any other URL after successful authentication

def features(request):
    return render(request, 'Features.html')
 

def pricing(request):
    return render(request, 'Pricing.html')

def contact(request):
    return render(request, 'Contact.html')