from datetime import datetime, timedelta
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from parkingapp.models import Spot, Lot, Vehicle, PaymentType, SpotReservation

@login_required
def lot_details(request, lot_id, user_id):
    if request.method == 'GET':

      lot = Lot.objects.get(pk=lot_id)

      lot.spots = Spot.objects.filter(lot_id=lot_id)

      payments = PaymentType.objects.filter(user_id=user_id)

      vehicles = Vehicle.objects.filter(user_id=user_id)

      template = 'lots/detail.html'

      context = {
        'lot': lot,
        'payments': payments,
        'vehicles': vehicles
      }

      return render(request, template, context)

    elif request.method == 'POST':

        form_data = request.POST

        lot = Lot.objects.get(pk=lot_id)

        """Getting number of hours reserved off of the form
        converting into an int, then getting current time and 
        adding the number of hours reserved to get the expiration
        time for the reservation
        """

        hours = int(form_data['num_of_hours'])
        current_time = datetime.now()
        hours_added = timedelta(hours=hours)
        exp_time = current_time + hours_added

        cost = lot.hourly_rate * hours

        spot = int(form_data['spot'])

        new_reservation = SpotReservation.objects.create(
          created_at = current_time,
          res_end_time = exp_time,
          total_cost = cost,
          spot_id = spot,
          payment_type_id = form_data['payment'],
          user_id = user_id,
          vehicle_id = form_data['vehicle']
        )

        return redirect(reverse('parkingapp:lot_list'))


