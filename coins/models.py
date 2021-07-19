from django.db import models


class Coin(models.Model):
    # base target timestamp price
    base = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    timestamp = models.IntegerField(default=0)
    price = models.FloatField(default=0, blank=True)

    def __str__(self):
        return str(self.base)+str(self.target)

    class Meta:
        ordering = ['-timestamp']


class Pair(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
