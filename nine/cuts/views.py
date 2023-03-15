from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.utils.http import is_safe_url
from django.contrib.auth import authenticate, login as auth_login

User=get_user_model()

def index(request):
	return render(request, 'cuts/home.html')

def login(request):
    form = LoginForm(request.POST or None)
    next_ = request.GET.get("next")
    next_post = request.POST.get("next")
    redirect_url = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
    context = {
        "form": form
    }
    return render(request, "/", context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        return redirect('/cuts/login/')
    context = {
        "form": form
    }
    return render(request, "cuts/signup.html", context)

def logout_page(request):
    logout(request)
    return redirect('/login')



def about(request):
	return render(request, 'cuts/about.html')


def cart(request):
	return render(request, 'cuts/cart.html')


def custom(request):
	return render(request, 'cuts/custom.html')


def why(request):
	return render(request, 'cuts/why.html')


def works(request):
	return render(request, 'cuts/works.html')


def guide(request):
	return render(request, 'cuts/guide.html')

def get_user_profile(request, username):
    username = User.objects.get(username=username)
    email = User.objects.get(email=email)
    return render(request, 'cuts/profile.html', {"user":user})