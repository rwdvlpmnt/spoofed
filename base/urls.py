from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('registration/login/', views.login_view, name='login'),  # Custom login view, ensure it doesn't conflict with auth
    path('registration/logout/', views.logout_view, name='logout'),  # Custom logout view
    path('register/', views.register, name='register'),  # Registration view
    path('profile/', views.profile, name='profile'),  # Profile view
    path('verify_email/', views.verify_email, name='verify_email'),  # Email verification view
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('phone-input/', views.phone_input, name='phone_input'),
    path('initiate_call/', views.initiate_call, name='initiate_call'),
    path('communicate/', views.communicate, name='communicate'),
    path('process-phone-numbers/', views.process_phone_numbers, name='process_phone_numbers'),
    path('navigation/', views.navigation, name='navigation'),
    path('terms/', views.terms, name='terms'),
    path('faq/', views.faq, name='faq'),
    path('blog/', views.blog, name='blog'),
    path('purchase/', views.purchase_with_stripe, name='purchase_with_stripe'),
    path('select_plan/', views.select_plan, name='select_plan'),

    # Removed the inclusion of auth and allauth URLs here to prevent redundancy
    # These should be included in the main URLs (phoneApp/urls.py) only
    # path('accounts/', include('django.contrib.auth.urls')),  # Commented out to prevent redundancy
    # path('accounts/', include('allauth.urls')),  # Commented out to prevent redundancy
]
