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
	light = models.CharField(max_length=12, choices=choices)
	flow = models.CharField(max_length=12, choices=choices)
	care = models.CharField(max_length=120)
	coral_type = models.ForeignKey("CoralType", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	@property
	def display_price(self):
		return "%s KD" % self.price

class OrderItem(models.Model):
	quantity = models.PositiveIntegerField(null=True)
	coral = models.ForeignKey("Coral", on_delete=models.CASCADE, default=1)
	cart = models.ForeignKey("OrderCheckout", on_delete=models.CASCADE, default=1, related_name="orderItems")

	def __str__(self):
		return "%s: %s" % (self.coral.name, str(self.quantity))

class OrderCheckout(models.Model):
	choices = (("Cash", "Cash"), ("Knet", "Knet"), ("Visa", "Visa"))
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	pyment_method=models.CharField(max_length=12, choices=choices, default="Knet")

	def __str__(self):
		return self.user.username
