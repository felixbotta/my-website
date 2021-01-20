from django.urls import path, include

from .views import *

app_name = 'core'
urlpatterns = [
    path('', about, name='about'),
    path('skills/', skills, name='skills'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
]
