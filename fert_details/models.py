from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Fertilizer(models.Model):

	name = models.CharField(max_length = 100)
	price = models.CharField(max_length = 50)
	shop_id = models.IntegerField()

  


class Shop_details(models.Model):
	shop_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 500)
	address = models.CharField(max_length = 500, unique = True)
	pincode = models.IntegerField()
	gst_no = models.CharField(max_length = 50,unique = True)
	ph_no = models.IntegerField()
	emailid = models.CharField(max_length = 50, unique = True)

 



		



		