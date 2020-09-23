from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

"""On request logs the user out and redirects them to the home page"""

def logout_user(request):
    logout(request)
    return redirect(reverse('parkingapp:home'))
