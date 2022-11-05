from django.db import models

class Flag(models.Model):
    ip_addr = models.CharField(max_length=30)
    flag = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_addr+' : '+self.flag
# Create your models here.
