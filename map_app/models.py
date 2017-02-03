from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GasStation(models.Model):
	station_name = models.CharField(max_length=200)
	gas_price = models.CharField(max_length=3)

	def __str__(self):
		return self.station_name

	class Meta:
		ordering = ('station_name',)

class Rest(models.Model):
	rest_name = models.CharField(max_length=200)
	rest_rating = models.CharField(max_length=1)

	def __str__(self):
		return self.rest_name

	class Meta:
		ordering = ('rest_name',)

class Store(models.Model):
	store_name = models.CharField(max_length=200)
	store_type = models.CharField(max_length=50)

	def __str__(self):
		return self.store_name

	def __unicode__(self):
		return self.store_name

	class Meta:
		ordering = ('store_name',)

class AreaLocation(models.Model):
	address = models.CharField(max_length = 150)
	zip_code = models.CharField(max_length=5, default='90051', blank=False, null=False)
	stations = models.ManyToManyField(GasStation, blank=True)
	rests = models.ManyToManyField(Rest, blank=True)
	stores = models.ManyToManyField(Store, blank=True)

	def __str__(self): 
		return self.address
