# flask
Flask Framework Files

This Repository includes a Project "BookEasy"
BookEasy is designed as a simple Flask Framework Project with below features

1. Flights Ticket Booking
2. User Sign Up / Account Creation
3. Login
4. Profile Editing
5. Profile/Account Deletion
6. Viewing Booked Ticket History

It assumes that MySQL is installed with user as "root" & password as ""
Make required modifications to the "credentials.py" file available in the "modules" folder to reflect the login credentials

Steps to run the Flask App

1. Download the Repository
2. Run / Start the MySQL Service in your machine
3. Update the "modules/credentials.py" file with the MySQL credentials
4. Run the "modules/delete_tables_db.py" file to clear any old data
5. Run the "modules/create_db_table_data.py" file to create DB, tables & sample data
6. Run the "app.py" to start the application for "BookNow" Web Application
7. Open your browser & go to the link "http://127.0.0.1:5000/" to launch the Web Application
8. You are ready to go!
