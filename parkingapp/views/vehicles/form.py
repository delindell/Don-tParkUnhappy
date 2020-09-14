from datetime import date
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from parkingapp.models import Vehicle

@login_required
def vehicle_form(request, user_id):
    if request.method == 'GET':
        
        template = 'vehicle/form.html'

        return render(request, template)

    elif request.method == 'POST':
        form_data = request.POST

        user = User.objects.get(pk=user_id)

        new_vehicle = Vehicle.objects.create(
          license_plate = form_data['license_plate'],
          make = form_data['make'],
          model = form_data['model'],
          color = form_data['color'],
          user = user
        )

        return redirect(reverse('parkingapp:vehicle_list', args=[user_id]))
