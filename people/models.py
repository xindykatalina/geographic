from django.db import models

# Create your models here.
class Person(models.Model): 
	first_name = models.CharField(max_length=255)
	nacionality = models.ManyToManyField('countries.Country')
	father = models.OneToOneField('self', on_delete=models.CASCADE, null=True )