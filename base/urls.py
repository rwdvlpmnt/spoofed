from django.urls import path, include 
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('registration/', include('django.contrib.auth.urls')),  # Include authentication URLs
    path('google-login/', views.google_login, name='google_login'),  # Adjust the URL and view name as per your implementation
    path('oauth/google/', views.google_oauth_view, name='google_oauth_url'),# Other URL patterns
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
  # path('keypad/', views.keypad, name='keypad'),
    path('contact/', views.contact, name='contact'),
    path('registration/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('phone-input/', views.phone_input, name='phone_input'),
    path('process-phone-numbers/', views.process_phone_numbers, name='process_phone_numbers'),                #...
    ]