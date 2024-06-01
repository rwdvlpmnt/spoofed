from django.shortcuts import render, redirect


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def logout(request):
    return render(request, 'logout.html')

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')
# Create your views here.

def google_login(request):
    # Logic for initiating Google OAuth authentication
    return redirect('google_oauth_url')  # Redirect to Google OAuth URL

def google_oauth_view(request):
    # Your Google OAuth logic here
    return redirect('home') # Redirect to 'home' or any other URL after successful authentication

def features(request):
    return render(request, 'features.html')
 
def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')

def phone_input(request):
    return render(request, 'phone_input.html')

def process_phone_numbers(request):
    if request.method == 'POST':
        number_to_call = request.POST.get('number_to_call')
        number_calling_from = request.POST.get('number_calling_from')
        my_number = request.POST.get('my_number')
        # Process the numbers as needed
        return redirect('phone_input')  # Redirect back to the form or another page
    return redirect('phone_input')

