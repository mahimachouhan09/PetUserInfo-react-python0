from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=60)
    age = models.SmallIntegerField()
    contact_number = models.CharField(max_length=12)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Pet(models.Model):
    pet_owner = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=60)
    type_of_pet = models.CharField(max_length=60)
    species = models.CharField(max_length=60)
    dob = models.DateField()
    intro = models.TextField()

    def __str__(self):
        return self.name