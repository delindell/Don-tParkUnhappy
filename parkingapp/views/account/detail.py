from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


@login_required
def account_details(request, user_id):

    """Upon request this function gets the logged in users information and
    passes it to the template"""

    if request.method == 'GET':

        auth_user = User.objects.filter(pk=user_id)

        template = 'account/detail.html'
        context = {
          'auth_user': auth_user
        }

        return render(request, template, context)

        
