# Updated views.py
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile  # Import Profile model
import json

# Signup View
@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            full_name = data.get('full_name')
            email = data.get('email')
            password = data.get('password')
            role = data.get('role')  # Added to accept role

            if User.objects.filter(username=email).exists():
                return JsonResponse({'error': 'User already exists'}, status=400)

            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = full_name
            user.profile.role = role  # Assuming role is stored in profile
            user.save()
            return JsonResponse({'message': 'Signup successful!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def student_login_view(request):
    if request.method == 'POST':
        try:
            # Load JSON data from request
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            # Validate input data
            if not email or not password:
                return JsonResponse({'error': 'Email and password are required.'}, status=400)

            # Authenticate the user
            user = authenticate(username=email, password=password)
            if user is None:
                return JsonResponse({'error': 'Invalid email or password.'}, status=401)

            # Check if the user has a student role
            if hasattr(user, 'profile') and user.profile.role == 'student':
                login(request, user)  # Log the user in
                return JsonResponse({'message': 'Student login successful!'}, status=200)
            else:
                return JsonResponse({'error': 'You are not authorized as a student.'}, status=403)

        except Exception as e:
            print("Error:", str(e))  # Print error to terminal for debugging
            return JsonResponse({'error': 'Something went wrong on the server.'}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

# Landlord Login View
@csrf_exempt
def landlord_login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            # Authenticate the landlord
            user = authenticate(username=email, password=password)
            if user is not None and hasattr(user, 'profile') and user.profile.role == 'landlord':
                login(request, user)
                return JsonResponse({'message': 'Landlord login successful!'}, status=200)
            return JsonResponse({'error': 'Invalid landlord credentials'}, status=401)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)
