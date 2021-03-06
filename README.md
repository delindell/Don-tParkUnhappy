# Don't Park Unhappy

## About the App

Don't Park Unhappy is an app developed for users(customers) and users(admin) alike, although with different capabilities. The customer is able to reserve parking spots in the Don't Park Unhappy lots. The app was also developed for users(admin) to be able add/view/delete/edit the companies parking lots/spots as needed. The admin can also view all active and expired reservations making it easy to tell who needs to be booted or towed if they have not vacated their spot before their reservation has expired. Users(customers) will be able to register/login and be authenticated safely with Django. Users(customers) are able to add payments, vehicles to their profile for ease of reserving the spot of their choosing upon arrival. The account tab has user(customer) information and is able to update their current information about their profile, payments, or vehicles. The reservations tab, only available to the admin user, also has a tally of the revenue the company has made from their parking lots.

## Downloading and Running the App

1. Create a new directory in your terminal. Clone down this repository by clicking the "Clone or Download" button above, copying the SSH key, and running the following command in your terminal `git clone sshKeyGoesHere`
2. `cd DontParkHappy`
3. Create your OSX virtual environment in Terminal:
    - `python -m venv parkingappEnv`
    - `source ./parkingappEnv/bin/activate`
- Or create your Windows virtual environment in Command Line:
    - `python -m venv parkingappEnv`
    - `source ./parkingappEnv/Scripts/activate`
4. Install the app's dependencies:
- `pip install -r requirements.txt`
5. Build your database from the existing models:
- `python manage.py makemigrations`
- `python manage.py migrate`
6. Create a superuser for your local version of the app:
- `python manage.py createsuperuser`
- This user will be the admin user for the app
7. Populate your database with initial data from fixtures files: (NOTE: every time you run this it will remove existing data and repopulate the tables)
- `python manage.py loaddata */fixtures/*.json`
8. Fire up your dev server and have some fun!
- `python manage.py runserver`

### Built With
* HTML
* CSS
* Django
* Python
* Bootstrap
* SQL

### ERD

![ERD](./screenshots/capstone_erd.png)

### Screenshots (for your viewing pleasure!)

##### Admin Active Reservations View

![ActiveReservations](./screenshots/active_reservations.png)

##### Admin Expired Reservations View

![ExpiredReservations](./screenshots/expired_reservations.png)

##### Customer Lot View

![Customer Lot View](./screenshots/lot_view_user.png)

##### Customer Lot Detail View

![Customer Lot Detail View](./screenshots/lot_details_user.png)


### Acknowledgements

I would personally like to thank all of my instructors and classmates, not only in Cohort 40, but in the Evening Cohort 11 as well, for helping to guide me on this arduous journey through Nashville Software School. I have met so many amazing, smart, talented indiviuals throughout this process that I can now call friends. Whilst this was personal effort undertaken by myself, I could not have done without your constant support and guidance. And for that I will be forever grateful.
