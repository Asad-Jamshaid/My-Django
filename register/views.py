from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register_page(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        
        # Check if the email is already in use
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already taken')
            return redirect('/register/')
        
        # Create a new User object and set the password
        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        
        # Save the user
        user.save()
        
        # Create the Registration object
        registration = Registration(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        registration.save()
        
        messages.success(request, f'Account created for {user.email}! You can now log in')
        return redirect('/login/')
    
    return render(request, 'register.html')



def login_page(request):
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        if not User.objects.filter(email=email).exists():
            messages.error(request, 'Invalid Email')
            return redirect('/login/')

        user = authenticate(request, username=email, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')

        login(request, user)
        return redirect('/home/')

    return render(request, 'login.html')

def logout_page(request):  
    logout(request)
    return redirect('/login/')
