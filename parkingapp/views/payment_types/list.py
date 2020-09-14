from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
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

    elif request.method == 'POST':

        form_data = request.POST

        if(
            "actual_method" in form_data
            and form_data["actual_method"] == 'DELETE'
        ):
          payment = PaymentType.objects.get(pk=int(form_data['payment_id']))
          payment.delete()

          return redirect(reverse('parkingapp:payment_list', args=[user_id]))

        return redirect(reverse('parkingapp:payment_list', args=[user_id]))
