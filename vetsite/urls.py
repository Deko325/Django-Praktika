from django.urls import path
from vetsite.views import *

urlpatterns = [
    path('', index, name='home'),
    path('catalog/', catalog),
    path('about/', about),
    path('contact/', contact, name='contact'),
    path('catalog/<int:pk>/', services, name='services'),
    path('doctor/', DoctorListView.as_view(), name='doctors'),
    path('doctor/<int:pk>', DoctorDetailView.as_view(), name='doctors_detail'),
]
