from django.db import models

# Create your models here.

class SupermarketModel(models.Model):
    http_method_names = ['post']
    item_lists =  models.CharField(max_length=1000)