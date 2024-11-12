from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {}
    return render(request, "home.html")

def portfolio_page(request):
    context = {}
    return render(request, "portfolio-details.html")

def service_page(request):
    context = {}
    return render(request, "service-details.html")

def starter_page(request):
    context = {}
    return render(request, "starter-page.html")

def about_page(request):
    context = {}
    return render(request, "about.html")

def team_page(request):
    context = {}
    return render(request, "team.html")

def testimonials_page(request):
    context = {}
    return render(request, "testimonials.html")

def pricing_page(request):
    context = {}
    return render(request, "pricing.html")

def faq_page(request):
    context = {}
    return render(request, "faq.html")

def contact_page(request):
    context = {}
    return render(request, "contact.html")