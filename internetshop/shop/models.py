from django.db import models


# Create your models here.
class Product(models.Model):
    objects = None
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.CharField(max_length=1024)

    speed = models.IntegerField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    material = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    author = models.CharField(max_length=256)
    rating = models.IntegerField()
    usage_duration = models.IntegerField()
    text = models.TextField()