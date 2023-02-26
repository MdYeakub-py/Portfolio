from django.db import models
from datetime import datetime

# Create your models here.
class InfoDetails(models.Model):
    birthday = models.CharField(max_length=40)
    age = models.CharField(max_length=3)
    website = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    degree = models.CharField(max_length=3)
    phone = models.CharField(max_length=14)
    city = models.CharField(max_length=5)
    freelance = models.CharField(max_length=9)


    # def __str__(self):
    #     return self.birthday

    # create models for Education



class Education(models.Model):
    start_date = models.DateField(default=datetime.now,blank=True)
    end_date = models.DateField(default=datetime.now,blank=True)
    degree_name =models.CharField(max_length=8)
    degree_in =models.CharField(max_length=50)
    details = models.CharField(max_length=60)

# create models for services

class Services(models.Model):
    logo = models.CharField(max_length=30)
    service_name = models.CharField(max_length=30)
    service_details = models.CharField(max_length=500)


# create models for project/protfolio
class Protfolio(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    title = models.CharField(max_length=40)
    images = models.FileField(upload_to='images/project_img/', max_length=250, null=True, default=None)
    def __str__(self):
        return self.id


# create models for contact information received

class AdminContact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.TextField()