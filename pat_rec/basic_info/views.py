from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    # Check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if user is valid
        user = authenticate(request, username=username, password=password)

        # If user is found, log them in
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {username}!")
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("index")
    else:
        return render(request, 'core/index.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("index")
