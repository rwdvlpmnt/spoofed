# your_app_name/utils.py

import random
import string
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile

def generate_verification_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def send_verification_email(user):
    verification_code = generate_verification_code()
    user.profile.verification_code = verification_code
    user.profile.save()
    subject = 'Email Verification'
    message = f'Your verification code is {verification_code}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
