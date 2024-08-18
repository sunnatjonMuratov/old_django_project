from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Added unique constraint

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Order categories by name

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name'] 
