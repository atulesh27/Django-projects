from django.db import models

# Create your models here.

class UserData(models.Model):
    name = models.CharField(max_length=210)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

