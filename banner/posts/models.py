from __future__ import unicode_literals
from django.utils import timezone
from datetime import datetime
from django.db import models
from django.db import models, migrations
import datetime
# Create your models here.

class Banners(models.Model):
	title = models.CharField(max_length=200)
	installment_price=models.IntegerField(null=True, blank=True)
	receiving_date=models.DateTimeField(null=True, blank=True)
	
	class Meta:
		verbose_name_plural= "Banners"

class Entry(models.Model):
	banner = models.ForeignKey(Banners, on_delete=models.CASCADE)
	booking_date = models.DateTimeField()
	end_booking_date= models.DateTimeField()
	total_price = models.IntegerField()
	no_of_installments = models.IntegerField()
	banner_installation_date= models.DateField()
	banner_removal_date= models.DateField()
	
	


	
	