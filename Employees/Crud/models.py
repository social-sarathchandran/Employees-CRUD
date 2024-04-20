from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to="photos/employees", blank=True, null=True)

    def __str__(self):
        return self.name
