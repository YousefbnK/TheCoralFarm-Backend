from django.db import models



class Coral_type(models.Model):
	name = models.CharField(max_length=120)
	image = models.ImageField(null=True)

	def __str__(self):
		return self.name



class Coral(models.Model):
	name = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=12, decimal_places=3)
	image = models.ImageField(null=True)
	Choice = (("L", "Low"), ("M", "Medium"), ("H", "High"))
	light = models.CharField(max_length=12, choices=Choice)
	flow = models.CharField(max_length=12, choices=Choice)
	care = models.CharField(max_length=120)
	coralType = models.ForeignKey("Coral_type", on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
  
	@property
	def display_price(self):
		return "%s KD" % self.price






