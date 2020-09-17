from datetime import datetime
from django.utils.timezone import get_current_timezone
from parkingapp.models import SpotReservation, Spot

def check_reservation():

    all_spots = Spot.objects.all()

    reserved_spots = all_spots.filter(is_reserved=True)

    reservations = SpotReservation.objects.all()

    current_time = datetime.now(tz=get_current_timezone())

    for spot in reserved_spots:
        for reservation in reservations:
           if spot.id == reservation.spot_id:
              if current_time > reservation.res_end_time:
                  spot.is_reserved = False
                  spot.save()
