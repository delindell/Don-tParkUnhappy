from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from parkingapp.models import Spot, Lot

@login_required
def lot_details(request, lot_id):
    if request.method == 'GET':

      lot = Lot.objects.get(pk=lot_id)

      lot.spots = Spot.objects.filter(lot_id=lot_id)

      template = 'lots/detail.html'

      context = {
        'lot': lot
      }

      return render(request, template, context)
