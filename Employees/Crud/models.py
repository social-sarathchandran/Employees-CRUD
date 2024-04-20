from django.db import models


class TimestampeModel(models.Model):
    """
    A mixin class add for 'create_date' and 'update_date'
    """

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Employee(TimestampeModel):
    """
    Model to represent the Employee

    1. name(str): Name of the employee
    2. email(str): Email address of the employee
    3. photo(Imagefiled): To store photo of employee(an optional field)

    """

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to="photos/employees", blank=True, null=True)

    def __str__(self):
        return f"{self.name}({self.email})"
