from django.urls import path
from mainapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("blog-details/", views.blogDetails, name="blogdetails"),
    path("services/", views.services, name="services"),
    path("services-details/", views.serviceDetails, name="servicedetails"),
    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq, name="faq"),
    path("terms/", views.terms, name="terms"),
    path("legal/", views.legal, name="legal"),
    path("privacy-policy/", views.privacyPolicy, name="privacy"),
    path("how-it-works/", views.howItworks, name="working"),
]