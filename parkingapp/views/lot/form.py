from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from parkingapp.models import Lot, Spot



@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_lot_form(request):
    if request.method == 'GET':
        template = 'lots/form.html'
        context = {}

        return render(request, template, context)

       

    elif request.method == 'POST':
        form_data = request.POST

        """Creating the new lot object and saving it to the database"""

        new_lot = Lot.objects.create(
          name = form_data['name'],
          address = form_data['address'],
          hourly_rate = form_data['hourly_rate']
        )

        """
        Here we are getting the number of spots in the new lot
        off of the form and converting that number into a list of individual numbers.
        Then making a new spot object for each one of those numbers in the list """

        num_of_spots = int(form_data['number_of_spots'])

        list_of_spots = [x for x in range(num_of_spots, 0, -1)]

        x = 0

        for spot in list_of_spots:
            x += 1
            new_spot = Spot.objects.create(
              number = x,
              is_reserved = False,
              lot_id = new_lot.id
            )

        return redirect(reverse('parkingapp:lot_list'))
