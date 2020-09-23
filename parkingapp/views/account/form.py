from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

@login_required
def edit_account_details(request, user_id):

    """Getting the users information and passing it to the edit profile template
    to prepopulate the form"""

    if request.method == 'GET':
        
        auth_user = User.objects.filter(pk=user_id)

        template = 'account/form.html'
        context = {
          'auth_user': auth_user
        }

        return render(request, template, context)

    elif request.method == 'POST':

        """Tricking the browser to update the users information
        by putting a hidden input field with the value PUT on the form. 
        Then saving the object to update it."""

        form_data = request.POST

        if(
            "actual_method" in form_data
            and form_data['actual_method'] == 'PUT'
        ):

            profile_to_update = User.objects.get(pk=user_id)

            profile_to_update.first_name = form_data["first_name"]
            profile_to_update.last_name = form_data["last_name"]
            profile_to_update.email = form_data["email"]

            profile_to_update.save()

            return redirect(reverse('parkingapp:account_details', args=[user_id]))

