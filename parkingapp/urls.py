from django.urls import path
from django.conf.urls import include
from parkingapp import views
from .views import *

app_name = 'parkingapp'
urlpatterns = [
    path('home/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('register/', register_form, name='register'),
    path('lots/', lot_list, name='lot_list'),
    path('lots/<int:lot_id>/', lot_details, name='lot_details'),
    path('lots/form/', add_lot_form, name='add_lot_form'),
    path('account/<int:user_id>/', account_details, name='account_details'),
    path('paymenttypes/<int:user_id>/', payment_list, name='payment_list'),
    path('paymenttypes/<int:user_id>/form/', payment_form, name='payment_form'),
]
