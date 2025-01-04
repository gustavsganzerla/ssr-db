from django.urls import path
from . import views


app_name = 'database'

urlpatterns = [
    path("home/", views.home, name = 'home'),
    path("query/", views.query, name = 'query'),
    path("about/", views.about, name = 'about'),
    path("contact/", views.contact, name = 'contact'),
    path("download_vntr/", views.download_vntr, name = 'download_vntr'),
    path("download_cssr/", views.download_cssr, name = 'download_cssr')
]
