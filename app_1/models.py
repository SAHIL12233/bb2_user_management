# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    address_choices = [('Home', 'Home'), ('Office', 'Office'), ('Other', 'Other')]
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    landline = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    is_primary = models.BooleanField(default=False)
    name = models.CharField(max_length=10, choices=address_choices, default='Home')

    def __str__(self):
        return self.name + "-" + self.street + " " + self.city + " " + self.state + " " + self.country + "-" + self.pincode


class UserPersonalDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    address = models.ManyToManyField(Address)

    def __str__(self):
        return self.name + " - " + self.phone


from django.db import models

# Create your models here.
