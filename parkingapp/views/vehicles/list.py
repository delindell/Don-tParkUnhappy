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
    
    elif request.method == 'POST':

        form_data = request.POST

        if(
            "actual_method" in form_data
            and form_data["actual_method"] == 'DELETE'
        ):
          vehicle = Vehicle.objects.get(pk=int(form_data['vehicle_id']))
          vehicle.delete()

          return redirect(reverse('parkingapp:vehicle_list', args=[user_id]))

