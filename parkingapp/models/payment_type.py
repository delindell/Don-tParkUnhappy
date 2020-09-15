from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class PaymentType(models.Model):

    merchant_name = models.CharField(max_length=50)
    account_num = models.CharField(max_length=19)
    account_last4 = models.CharField(max_length=20)
    expiration_date = models.CharField(max_length=5)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Meta:
    verbose_name = ("payment_type")
    verbose_name_plural = ("payment_types")

    def __str__(self):
        return self.merchant_name

    def get_absolute_url(self):
        return reverse("payment_type_detail", kwargs={"pk": self.pk})
