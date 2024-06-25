from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

def login_view(request):
    return render(request, 'login.html')

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def register(request):
    return render(request, 'register.html')

def logout_view(request):
    return render(request, 'logout.html')

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def google_login(request):
    return redirect('google_oauth_url')

def google_oauth_view(request):
    return redirect('home')

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
        return redirect('phone_input')
    return redirect('phone_input')

def navigation(request):
    return render(request, 'navigation.html')

def terms(request):
    return render(request, 'terms.html')

def faq(request):
    return render(request, 'faq.html')

def blog(request):
    return render(request, 'blog.html')

def facebook_login(request):
    return HttpResponse("Facebook login view")

@csrf_exempt
def purchase_with_stripe(request):
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Phone Credits',
                    },
                    'unit_amount': 1000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        return redirect(session.url, code=303)
    return render(request, 'stripe.html')

@login_required
def initiate_call(request):
    if request.method == 'POST':
        to_number = request.POST['to_number']
        from_number = request.POST['from_number']
    return render(request, 'initiate_call.html')

@login_required
def communicate(request):
    return render(request, 'communicate.html')
