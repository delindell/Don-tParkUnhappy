from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def register_form(request):
    if request.method == 'GET':
        template = 'registration/form.html'
        context = {}

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_user = User.objects.create_user(
            username = form_data['username'],
            email = form_data['email'],
            password = form_data['password'],
            first_name = form_data['first_name'],
            last_name = form_data['last_name']
        )

        return redirect(reverse('parkingapp:home'))

