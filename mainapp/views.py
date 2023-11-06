from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def blogDetails(request):
    return render(request, "blog-details.html")

def services(request):
    return render(request, "services.html")

def serviceDetails(request):
    return render(request, "service-details.html")

def contact(request):
    return render(request, "contact.html")

def faq(request):
    return render(request, "faq.html")

def terms(request):
    return render(request, "terms.html")

def legal(request):
    return render(request, "legal.html")

def privacyPolicy(request):
    return render(request, "privacy-policy.html")

def howItworks(request):
    return render(request, "how-it-works.html")
