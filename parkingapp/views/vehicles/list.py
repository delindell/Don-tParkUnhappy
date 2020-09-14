from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from parkingapp.models import Vehicle

@login_required
def vehicle_list(request, user_id):
    if request.method == 'GET':
        
        user = User.objects.get(pk=user_id)

        vehicles = Vehicle.objects.filter(user_id=user.id)

        template = 'vehicle/list.html'
        context = {
          'vehicles': vehicles
        }

        return render(request, template, context)
