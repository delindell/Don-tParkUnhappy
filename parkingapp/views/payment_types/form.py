from datetime import date
from django import forms
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

        """Here we are formating the actual CC number to just 
        show the last 4 digits on the template, whilst still storing
        the actual number in the DB"""

        get_cc_last4 = form_data['account_num'].split()[-1]
      
        cc_last4 = '{} {}'.format('xxxxxxxxxxxx', get_cc_last4)

        expiry = '{}/{}'.format(form_data['expireMM'], form_data['expireYY'])

        new_payment = PaymentType.objects.create(
          merchant_name = form_data['merchant_name'],
          account_num = form_data['account_num'],
          account_last4 = cc_last4,
          expiration_date = expiry,
          created_at = date.today(),
          user = user
        )

        return redirect(reverse('parkingapp:payment_list', args=[user_id]))
