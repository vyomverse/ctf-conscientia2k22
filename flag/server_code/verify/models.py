from django.db import models

class Flag(models.Model):
    ip_addr = models.CharField(max_length=30)
    flag = models.CharField(max_length=30)
    valid = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_addr+' : ' + self.flag + ' is ' + str(self.valid)
# Create your models here.
