from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from parkingapp.models import Lot



@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_lot_form(request):
    if request.method == 'GET':
        template = 'lots/form.html'
        context = {}

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_lot = Lot.objects.create(
          name = form_data['name'],
          address = form_data['address'],
          open_time = form_data['open_time'],
          close_time = form_data['close_time'],
          hourly_rate = form_data['hourly_rate']
        )

        return redirect(reverse('parkingapp:lot_list'))
