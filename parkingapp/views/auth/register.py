from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def register_form(request):
    if request.method == 'GET':
        template = 'registration/form.html'
        context = {}

        return render(request, template, context)

    elif request.method == 'POST':

        """Creating a new user object in the DB"""

        form_data = request.POST

        new_user = User.objects.create_user(
            username = form_data['username'],
            email = form_data['email'],
            password = form_data['password'],
            first_name = form_data['first_name'],
            last_name = form_data['last_name']
        )

        """Logging in the user on completition of registration"""

        authenticated_user = authenticate(username=form_data['username'], password=form_data['password'])

        if authenticated_user is not None:
            login(request, authenticated_user)

        return redirect(reverse('parkingapp:lot_list'))

