from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.home_page, name="home"),
    path('portfolio/', views.portfolio_page, name="portfolio"),
    path('service/', views.service_page, name="service"),
    path('starter/', views.starter_page, name="starter"),
    path('about/', views.about_page, name="about"),
    path('team/', views.team_page, name="team"),
    path('pricing/', views.pricing_page, name="pricing"),
    path('faq/', views.faq_page, name="faq"),
    path('testimonials/', views.testimonials_page, name="testimonials"),
    path('contact/', views.contact_page, name="contact"),
]
