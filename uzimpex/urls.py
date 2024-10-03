from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('documents/', documents, name='documents'),
    path('services/', services, name='services'),
    path('services/<str:slug>/', services_detail, name='services_detail'),
    path('about/', about, name='about'),
    path('message_uz/', message_uz, name='message_uz'),
    path('message_en/', message_en, name='message_en'),
    path('about/otdeli', department, name='department'),
    path('about/rukovodstvo', ruk, name='ruk'),
    path('useful_links/', useful_links, name='useful_links')

]
