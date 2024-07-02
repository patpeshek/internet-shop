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
    material = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name
