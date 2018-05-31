from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        "title": "Test message",
        "content": "Welcome to home_page"
    }
    return render(request,"home_page.html",context)


def about_page(request):
    context = {
        "title": "about_page",
        "content": "Welcome to about_page"
    }
    return render(request, "about_page.html", context)


def contact_page(request):
    context = {
        "title": "contact_page",
        "content": "Welcome to contact_page"
    }
    return render(request, "contact_page.html",context)
