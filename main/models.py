from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    desciption = models.TextField()
    shade = models.TextField()
    size = models.TextField()

    @property
    def is_product_ready(self):
        return self.mood_intensity > 5