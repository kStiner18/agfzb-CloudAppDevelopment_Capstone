from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def contact(request):
    # Your logic for the contact view goes here
    return render(request, 'djangoapp/contact.html')

def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'djangoapp/login.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('djangoapp:index')

def registration_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('djangoapp:login')
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/register.html', {'form': form})

def get_dealer_details(request, dealer_id):
    # Implement your logic here
    return render(request, 'djangoapp/dealer_details.html')

def add_review(request, dealer_id):
    # Implement your logic here
    return render(request, 'djangoapp/add_review.html')

def get_dealerships(request):
    # Your logic for the get_dealerships view goes here
    return render(request, 'djangoapp/dealerships.html')

def my_view(request):
    # Your logic for the my_view goes here
    return render(request, 'djangoapp/my_view.html')

def about_view(request):
    # Your logic for the about_view goes here
    return render(request, 'djangoapp/about.html')