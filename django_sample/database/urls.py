from django.urls import path
from . import views


app_name = 'database'

urlpatterns = [
    path("home/", views.home, name = 'home'),
    path("query/", views.query, name = 'query'),
    path("about/", views.about, name = 'about'),
    path("contact/", views.contact, name = 'contact')
]
