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
    #test_to_ send_data
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, "contact/view.html",context)
