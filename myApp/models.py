from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, primary_key=True, unique=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    

    def __str__(self) -> str:
        return self.name