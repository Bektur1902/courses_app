from django.db import models

# Create your models here.

CONTACT_CHOISES = (
    (1, 'PHONE'),
    (2, 'FACEBOOK'),
    (3, 'EMAIL')
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    imgpath = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    logo = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course')

    def __str__(self) -> str:
        return self.name

class Branch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')
    latitude = models.CharField(max_length=100)
    longtude = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.address

class Contact(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts')
    type = models.IntegerField(choices=CONTACT_CHOISES, blank=True, null=True)
    value = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.value
