from django.db import models
from django.shortcuts import reverse

class Lot(models.Model):
    
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    hourly_rate = models.IntegerField()

    class Meta:
        verbose_name = ("lot")
        verbose_name_plural = ("lots")

    def get_absolute_url(self):
        return reverse("lot_detail", kwargs={"pk": self.pk})
