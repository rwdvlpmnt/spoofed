from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import login
from .forms import RegistrationForm
from .models import Profile
from .utils import send_verification_email

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
@require_POST
def create_checkout_session(request):
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

    # Example of using the session ID to retrieve a payment intent
    # intent = stripe.PaymentIntent.retrieve(session.payment_intent)
    # print(intent.client_secret)   # print(intent.client_secret)

    # Example of using the session ID to create a customer
    # customer = stripe.Customer.create(
    #     email=request.POST['email'],
    #     payment_method=request.POST['payment_method_id'],
    #     invoice_settings={
    #         'default_payment_method': request.POST['payment_method_id'],
    #     },
    # )
    # print(customer.id)  # print(customer.id)

def login_view(request):
    return render(request, 'login.html')

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'registration/login.html')

def logout_view(request):
    return render(request, 'registration/logout.html')


@login_required
def profile(request):
    return render(request, 'profile.html')

def features(request):
    return render(request, 'features.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')

def phone_input(request):
    return render(request, 'phone_input.html')

@login_required
def initiate_call(request):
    return render(request, 'initiate_call.html')

@login_required
def communicate(request):
    return render(request, 'communicate.html')

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

@require_POST
def select_plan(request):
    price = request.POST.get('price')
    # Prepare any additional data needed for Stripe
    return render(request, 'stripe.html', {'price': price})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until it is verified
            user.save()
            Profile.objects.create(user=user)
            send_verification_email(user)
            return redirect('verify_email')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def verify_email(request):
    if request.method == 'POST':
        code = request.POST['verification_code']
        try:
            profile = Profile.objects.get(verification_code=code)
            profile.user.is_active = True
            profile.user.save()
            login(request, profile.user)
            return redirect('home')
        except Profile.DoesNotExist:
            return render(request, 'verify_email.html', {'error': 'Invalid verification code'})
    return render(request, 'verify_email.html')