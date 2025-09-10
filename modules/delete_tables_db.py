import mysql.connector
from credentials import * # local module file

#establsih connection
con=mysql.connector.connect(host = host ,username = username , password = password,charset=charset)
                            
if con.is_connected():
     print("Connected Successfully!")


#create cursor
cur=con.cursor()


# Delete User table
sql=f"""DROP TABLE IF EXISTS {database}.{table_user}"""
cur.execute(sql)
print("User Table deleted successfully.")

# Delete Flights table
sql=f"""DROP TABLE IF EXISTS {database}.{table_flights}"""
cur.execute(sql)
print("Flights Table deleted successfully.")

# Delete Bookings table
sql=f"""DROP TABLE IF EXISTS {database}.{table_bookings}"""
cur.execute(sql)
print("Bookings Table deleted successfully.")

# Delete the entire database
sql=f"""DROP DATABASE IF EXISTS {database}"""
cur.execute(sql)
print("Database deleted successfully.")


#close the cursor
cur.close()

#close the connection
con.close()

