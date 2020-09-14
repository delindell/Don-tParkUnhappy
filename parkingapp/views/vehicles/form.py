from datetime import date
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from parkingapp.models import Vehicle

@login_required
def vehicle_form(request, user_id):
  pass
