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
    path('lots/<int:lot_id>/', lot_details, name='lot_details')
]
