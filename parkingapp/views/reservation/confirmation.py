from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from parkingapp.models import SpotReservation


def reservation_confirmation(request, reservation_id):
    if request.method == 'GET':

        reservation = SpotReservation.objects.get(pk=reservation_id)

        formated_exp_time = reservation.res_end_time.ctime()

        template = 'reservation/confirmation.html'

        context = {
          'reservation': reservation,
          'expire_time': formated_exp_time
        }
        
        return render(request, template, context)
