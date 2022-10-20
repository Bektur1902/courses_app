from django.db import models

# Create your models here.

CONTACT_CHOISES = (
    (1, 'PHONE'),
    (2, 'Facebook'),
    (3, 'Email')
)

class Course(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    logo = models.CharField(max_length=100, blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    imgpath = models.CharField(max_length=100)

class Branch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=100)
    longtude = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

class Conctact(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.IntegerField(choices=CONTACT_CHOISES, blank=True, null=True)
    value = models.CharField(max_length=100)
