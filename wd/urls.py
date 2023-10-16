from django.urls import path
from . import views

urlpatterns = [
    path('',views.check_phishing,name='check_phishing'),
    path('sql_injection/',views.check_sqlinjection,name='sql_injection'),
    
    path('list-website/', views.list_suspicious_websites, name='list_website'),
    path('list_sqli/', views.list_sqliwebsites, name='list_sqli'),
    
]