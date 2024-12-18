# Updated project-level urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to SamiStay!")

urlpatterns = [
    path('admin/', admin.site.urls),      # Django admin
    path('', home_view, name='home'),     # Root path
    path('api/', include('login.urls')),  # Include app-level URLs with 'api/' prefix
]
