import mysql.connector
from credentials import * # local module file

#establish connection
con=mysql.connector.connect(host = host ,username = username , password = password,charset=charset)
                            
if con.is_connected():
     print("Connected Successfully!")


#create cursor
cur=con.cursor()


#use database
sql=f"""use {database}"""
cur.execute(sql)


#view user table data
sql=f"""select * from {table_user}"""
cur.execute(sql)
print("User Master")
print("-----------")
for i in cur:
     print(i)
print("\n")


#view flight table data
sql=f"""select * from {table_flights}"""
cur.execute(sql)
print("Flight Master")
print("-------------")
for i in cur:
     print(i)
print("\n")

#view booking table data
sql=f"""select * from {table_bookings}"""
cur.execute(sql)
print("Booking Master")
print("--------------")
for i in cur:
     print(i)
print("\n")

#close the cursor
cur.close()

#close the connection
con.close()

