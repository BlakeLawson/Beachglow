from django.db import models

# Create your models here.
class Sale(models.Model):
	product = models.CharField(max_length=50)
	time = models.CharField(max_length=50)
	