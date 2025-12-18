from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from ourguardsnew.models import Ourguards



def countriesData(request):
    # Import requests locally to avoid import-time module loading issues
    import requests

    api_url = "https://api.first.org/data/v1/countries"

    response = requests.get(api_url)
    if response.status_code == 200:
        countries_Data = response.json()
        countries = countries_Data.get('data', {})
    else:
        countries = {}
    return render(request, 'print_json.html', {'countries': countries}) 


def HomePage(request):
    guards = Ourguards.objects.all()
    return render(request, 'index.html', {'guards': guards})


def AboutPage(request):
    return render(request, 'about.html')


def ServicePage(request):
    return render(request, 'service.html')


def PricingPage(request):
    return render(request, 'pricing.html')


def BlogPage(request):
    return render(request, 'blog.html')


def SinglePage(request):
    return render(request, 'single.html')


def ContactPage(request):
    return render(request, 'contact.html')



