from django.db import models

# Create your models here.

class payloadModel(models.Model):
    symbol = models.TextField()
    price = models.IntegerField()
    timestamp = models.BigIntegerField()

    def __str__(self):
        return str(self.symbol) + " - " + str(self.price) + " - " + str(self.timestamp)