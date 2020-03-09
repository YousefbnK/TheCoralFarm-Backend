from django.db import models



class Item(models.Model):
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=12, decimal_places=3)
	image = models.ImageField()
	light = models.CharField(max_length=120)
	flow = models.CharField(max_length=120)
	care = models.CharField(max_length=120)
	coralType = models.ForeignKey("CoralType", on_delete=models.CASCADE)
	
	
	def __str__(self):
		return self.name
	
	@property
	def display_price(self):
		return "%s KD" % self.price


class CoralType(models.Model):
	name = models.CharField(max_length=120)
	image = models.ImageField()


	def __str__(self):
		return self.name






