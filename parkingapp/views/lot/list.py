from datetime import datetime
from django.utils.timezone import get_current_timezone
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from parkingapp.models import Lot
from ...helpers import check_reservation

@login_required
def lot_list(request):
    if request.method == 'GET':

        check_reservation()

        all_lots = Lot.objects.all()

        template_name = 'lots/list.html'

        context = {
          'all_lots': all_lots
        }

        return render(request, template_name, context)


    elif request.method == 'POST':

        form_data = request.POST

        if(
          "actual_method" in form_data
          and form_data["actual_method"] == 'DELETE'
        ):

          lot = Lot.objects.get(pk=int(form_data['lot_id']))
          lot.delete()

          return redirect(reverse('parkingapp:lot_list'))
