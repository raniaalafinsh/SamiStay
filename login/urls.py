from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.signup_view, name='signup'),  # Maps to /api/signup/
    path('login/student/', views.student_login_view, name='student_login'),  # Student login
    path('login/landlord/', views.landlord_login_view, name='landlord_login'),  # Landlord login


]

