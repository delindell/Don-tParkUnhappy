from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.timezone import get_current_timezone
from parkingapp.models import SpotReservation, Lot, Spot

def reservation_list(request):
    if request.method == 'GET':

        all_reservations = SpotReservation.objects.all()

        all_spots = Spot.objects.all()

        reserved_spots = all_spots.filter(is_reserved=True)

        expired_spots = all_spots.filter(is_reserved=False)

        current_time = datetime.now(tz=get_current_timezone())

        total_revenue = 0

        for reservation in all_reservations:
            total_revenue += int(reservation.total_cost)

        template = 'reservation/list.html'

        context = {
          'all_reservations': all_reservations,
          'all_spots': all_spots,
          'current_time': current_time,
          'total_revenue': total_revenue
        }

        return render(request, template, context)

