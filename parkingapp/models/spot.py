from django.db import models
from django.shortcuts import reverse
from safedelete.models import SOFT_DELETE, SafeDeleteModel
from .lot import Lot

class Spot(SafeDeleteModel):

    number = models.IntegerField()
    is_reserved = models.BooleanField(default=None)
    lot = models.ForeignKey(Lot, verbose_name=("lot"), on_delete=models.CASCADE)
    _safedelete_policy = SOFT_DELETE

    class Meta:
        verbose_name = ("spot")
        verbose_name_plural = ("spots")

    def get_absolute_url(self):
        return reverse("spot_detail", kwargs={"pk": self.pk})
