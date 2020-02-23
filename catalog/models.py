from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Product(models.Model):
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False)
    price = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
    Category = models.ForeignKey("Category", blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(blank=False, default=0)
    image = ImageField(blank=True)
    
    def __str__(self):
        return self.name + " $" + str(self.price)
    

# Create Category Field
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Categories"
        