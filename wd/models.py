from django.db import models

class SuspiciousWebsite(models.Model):
    url = models.URLField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        # Retrieve the numerical index by counting the existing objects with older timestamps
        index = SuspiciousWebsite.objects.filter(created_at__lte=self.created_at).count()
        return f"{index} - {self.url}"
