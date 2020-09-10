from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Vehicle(models.Model):

    license_plate = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Meta:
    verbose_name = ("vehicle")
    verbose_name_plural = ("vehicles")

    def __str__(self):
        return self.license_plate

    def get_absolute_url(self):
        return reverse("vehicle_detail", kwargs={"pk": self.pk})
