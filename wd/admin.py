from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SuspiciousWebsite
from .models import SqlinjectedWebsite

admin.site.register(SqlinjectedWebsite)

admin.site.register(SuspiciousWebsite)
