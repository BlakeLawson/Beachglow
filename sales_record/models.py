from django.db import models

class Sale(models.Model):
	product = models.CharField(max_length=50)
	time = models.CharField(max_length=50)