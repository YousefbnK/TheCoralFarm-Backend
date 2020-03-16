from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class CoralType(models.Model):
	name = models.CharField(max_length=120)
	image = models.ImageField(null=True)

	def __str__(self):
		return self.name



class Coral(models.Model):
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=12, decimal_places=3)
	image = models.ImageField(null=True)
	choices = (("L", "Low"), ("M", "Medium"), ("H", "High"))
	light = models.CharField(max_length=12, choices= choices)
	flow = models.CharField(max_length=12, choices=choices)
	care = models.CharField(max_length=120)
	coral_type = models.ForeignKey("CoralType", on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
  
	@property
	def display_price(self):
		return "%s KD" % self.price

class Order(models.Model):
	quantity = models.PositiveIntegerField(null=True)
	coral = models.ForeignKey("Coral", on_delete=models.CASCADE, default=1)
	cart = models.ForeignKey("Checkout", on_delete=models.CASCADE, default=1)

	def __str__(self):
		return "%s: %s" % (self.coral.name, str(self.quantity))

class Checkout(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	# item = models.ManyToManyField(Order)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.user.username


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)
  






