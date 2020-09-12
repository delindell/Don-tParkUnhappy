from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from parkingapp.models import PaymentType

@login_required
def payment_list(request, user_id):
    if request.method == 'GET':

        user = User.objects.get(pk=user_id)

        payment_types = PaymentType.objects.filter(user_id=user.id)

        template = 'payment/list.html'
        context = {
          'payment_types': payment_types
        }

        return render(request, template, context)
