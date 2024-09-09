from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    desciption = models.TextField()
    quantity = models.IntegerField()
    # time = models.DateField(auto_now_add=True)
    # feelings = models.TextField()
    # mood_intensity = models.IntegerField()

    @property
    def is_product_ready(self):
        return self.mood_intensity > 5