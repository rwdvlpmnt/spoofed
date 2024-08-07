from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),  # Main app URLs
    # Choose one set of authentication URLs
    path('accounts/', include('allauth.urls')),  # Use this if preferring allauth
    # path('accounts/', include('django.contrib.auth.urls')),  # Or use this if preferring built-in auth
]
