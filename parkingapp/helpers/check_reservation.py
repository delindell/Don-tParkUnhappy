from datetime import datetime
from django.utils.timezone import get_current_timezone
from parkingapp.models import SpotReservation, Spot

def check_reservation():

    """
    When called this helper function gets all the spots that are
    currently reserved, then gets all the spot reservations. Matches
    the spot with the reservation, then compares if the current time 
    is greater than when the reservation is scheduled to end. If this
    is true it will change the is_reserved field on the spot object to
    False
    """

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
