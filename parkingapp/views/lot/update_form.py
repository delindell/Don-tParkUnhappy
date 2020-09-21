from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from parkingapp.models import Lot

def lot_update_form(request, lot_id):
    if request.method == 'GET':

        lot = Lot.objects.get(pk=lot_id)

        template = 'lots/update_form.html'
        context = {
          'lot': lot
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if(
          'actual_method' in form_data
          and form_data['actual_method'] == 'PUT'
        ):

          lot_to_update = Lot.objects.get(pk=lot_id)

          lot_to_update.name = form_data["name"]
          lot_to_update.address = form_data['address']
          lot_to_update.hourly_rate = form_data['hourly_rate']

          lot_to_update.save()

          return redirect(reverse('parkingapp:lot_list'))
