from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    title = models.TextField(max_length=100)
    price = models.IntegerField(default=50)

    def __str__(self):
        return self.name

