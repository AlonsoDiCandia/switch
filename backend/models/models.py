import uuid
from django.db import models

# Create your models here.

class Bulb(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    external_id = models.CharField(max_length=30)
    ip = models.CharField(max_length=16)
    port = models.IntegerField()
    power = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class House(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()



    

