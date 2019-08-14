from django.db import models
class register(models.Model):

    UserName = models.CharField(max_length=10)
    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    DateOfJoin = models.DateField()
    Email = models.EmailField()
    MobileNumber = models.IntegerField()
    Password = models.CharField(max_length=10)
    ConfirmPassword = models.CharField(max_length=10)

# Create your models here.
