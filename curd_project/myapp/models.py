from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    address = models.TextField()




    def __str__(self):
        return self.name
