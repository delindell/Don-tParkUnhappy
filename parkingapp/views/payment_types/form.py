from datetime import date
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from parkingapp.models import PaymentType


@login_required
def payment_form(request, user_id):
    if request.method == 'GET':
        template = 'payment/form.html'

        return render(request, template)

    elif request.method == 'POST':
        form_data = request.POST

        user = User.objects.get(pk=user_id)

        new_payment = PaymentType.objects.create(
          merchant_name = form_data['merchant_name'],
          account_num = form_data['account_num'],
          expiration_date = form_data['expiration_date'],
          created_at = date.today(),
          user = user
        )

        return redirect(reverse('parkingapp:payment_list', args=[user_id]))
