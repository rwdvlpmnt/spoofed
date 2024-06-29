from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home view
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),  # Profile view
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
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth URLs
    path('accounts/', include('allauth.urls')),  # Django Allauth URLs
    path('select_plan/', views.select_plan, name='select_plan'),  # Add this line for the select_plan view
]
