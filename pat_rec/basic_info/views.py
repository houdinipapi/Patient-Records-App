from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Patient


# Create your views here.

def index(request):
    patients = Patient.objects.all()


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
        return render(request, 'core/index.html',
                      {
                          "patients": patients
                      })


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("index")


def sign_up(request):
    # Check to see if signing up
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and log user in
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(request, username=username, password=password)

            login(request, user)

            messages.success(request, f"Welcome, {username}!")
            return redirect("index")
    else:
        form = SignUpForm()
        return render(request, 'core/signup.html', {
            "form": form
        })
    
    return render(request, 'core/signup.html', {
        "form": form
    })

