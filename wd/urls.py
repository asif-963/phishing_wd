from django.urls import path
from . import views

urlpatterns = [
    path('',views.check_phishing,name='check_phishing'),
    path('list-website/', views.list_suspicious_websites, name='list_website'),
    
]