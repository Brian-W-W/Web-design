from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    Id = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    #banner = models.ImageField(upload_to=='images/', blank=True)


    