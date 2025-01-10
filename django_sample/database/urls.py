from django.urls import path
from . import views


app_name = 'database'

urlpatterns = [
    path("home/", views.home, name = 'home'),
    path("query/", views.query, name = 'query'),
    path("statistics/", views.statistics, name = 'statistics'),
    path("faq/", views.faq, name = 'faq'),
    path("about/", views.about, name = 'about'),
    path("contact/", views.contact, name = 'contact'),
    path("download_vntr/", views.download_vntr, name = 'download_vntr'),
    path("download_cssr/", views.download_cssr, name = 'download_cssr'),
    path("download_issr/", views.download_issr, name = 'download_issr'),
    path("download_ssr/", views.download_ssr, name = 'download_ssr')
]
