import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=255)
    shade = models.TextField(max_length=255)
    size = models.TextField(max_length=255)

    @property
    def is_product_ready(self):
        return self.price > 5