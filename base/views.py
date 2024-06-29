from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'registration/login.html')

def logout_view(request):
    return render(request, 'registration/logout.html')

def register(request):
    return render(request, 'registration/register.html')

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