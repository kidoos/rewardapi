from django.db import models

# Create your models here.

class TransactionDetail(models.Model):
    customer_id = models.IntegerField(blank=False)
    customer_name= models.CharField(max_length=100)
    purchase_date = models.DateField(auto_now_add=True)
    purchase_amount = models.IntegerField()
    reward_points = models.IntegerField()

