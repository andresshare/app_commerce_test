from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
        "title": "Test message",
        "content": "Welcome to home_page",
        "premium_content":"you hace access rigth PREMIUM"
    }

    return render(request,"home_page.html",context)


def about_page(request):
    context = {
        "title": "about_page",
        "content": "Welcome to about_page"
    }
    return render(request, "about_page.html", context)


def contact_page(request):
    #instance form
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "contact_page",
        "content": "Welcome to contact_page",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    #test_to_ send_data
    #if request.method == 'POST':
        #print(request.POST)
        #print(request.POST.get('fullname'))
        #print(request.POST.get('email'))
        #print(request.POST.get('content'))
    return render(request, "contact/view.html",context)



def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    #print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        #print(request.user.is_authenticated())
        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)
        # Redirect to a success page.
            return redirect("/login")
        else:
        # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)


def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", {})
