from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about.html', views.about, name='about'),
	path('service.html', views.service, name='service'),
	path('pricing.html', views.pricing, name='pricing'),
	path('contact.html', views.contact, name='contact'),
	path('appointment.html', views.appointment, name='appointment'),
]
