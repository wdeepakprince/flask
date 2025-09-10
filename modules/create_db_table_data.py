import mysql.connector
from credentials import * # local module file


#establish connection
con=mysql.connector.connect(host = host ,username = username , password = password,charset=charset)
                            
if con.is_connected():
     print("Connected Successfully!")
print("\n")

#create cursor
cur=con.cursor()


#create database
sql=f"""create database {database}"""
cur.execute(sql)


#use database
sql=f"""use {database}"""
cur.execute(sql)

# ---------------- USER ------------------------------------

#create table, data rows
sql=f"""create table {table_user} (Username varchar(20),Password varchar(20),FullName varchar(20), EMail varchar(20))"""
cur.execute(sql)

#create data rows
sql=f"""insert into {table_user} values ('deepak', 'dp', 'Deepak', 'deepak@gmail.com')"""
cur.execute(sql)

sql=f"""insert into {table_user} values ('prince', 'pr', 'Prince', 'prince@gmail.com')"""
cur.execute(sql)

sql=f"""insert into {table_user} values ('barathi', 'ba', 'Barathi', 'barathi@gmail.com')"""
cur.execute(sql)

sql=f"""insert into {table_user} values ('jacob', 'jc', 'Jacob', 'jacob@gmail.com')"""
cur.execute(sql)

sql=f"""insert into {table_user} values ('joanna', 'jo', 'Joanna', 'joanna@gmail.com')"""
cur.execute(sql)


#commit all changes
con.commit()

#view table data
sql=f"""select * from {table_user}"""
cur.execute(sql)

print("User Master")
print("-----------")
for i in cur:
     print(i)

print("\n")

# ---------------- FLIGHTS ------------------------------------

#create table, data rows
sql=f"""create table {table_flights} (FlightNumber varchar(20),FromStation varchar(20),ToStation varchar(20), DepartureTime time, ArrivalTime time, TicketCost int)"""
cur.execute(sql)

#create data rows
sql=f"""insert into {table_flights} values ('BE-CJB-IXM', 'Coimbatore', 'Madurai', '06:30:00', '07:30:00', 5500)"""
cur.execute(sql)

sql=f"""insert into {table_flights} values ('BE-IXM-TRZ', 'Madurai', 'Tiruchirappalli',  '07:00:00', '07:45:00', 2500)"""
cur.execute(sql)

sql=f"""insert into {table_flights} values ('BE-TRZ-TCR', 'Tiruchirappalli', 'Tuticorin',  '08:30:00', '09:50:00', 3000)"""
cur.execute(sql)

sql=f"""insert into {table_flights} values ('BE-IXM-MAA', 'Madurai', 'Chennai', '09:00:00', '10:30:00', 6750)"""
cur.execute(sql)

sql=f"""insert into {table_flights} values ('BE-MAA-SXV', 'Chennai', 'Salem', '10:00:00', '11:30:00', 5725)"""
cur.execute(sql)


#commit all changes
con.commit()

#view table data
sql=f"""select * from {table_flights}"""
cur.execute(sql)

print("Flight Master")
print("-------------")
for i in cur:
     print(i)

print("\n")



# ---------------- BOOKINGS ------------------------------------

#create table, data rows
sql=f"""create table {table_bookings} (BookingID INT AUTO_INCREMENT PRIMARY KEY,Username varchar(20), FlightNumber varchar(20),TravelDate Date,TicketCount int, TotalPrice int, Status varchar(20))"""
cur.execute(sql)

#create data rows
sql=f"""insert into {table_bookings} (Username, FlightNumber, TravelDate, TicketCount, TotalPrice, Status) values ('deepak', 'BE-IXM-MAA', '2025-10-01', 2, 13500,'Confirmed')"""
cur.execute(sql)

sql=f"""insert into {table_bookings} (Username, FlightNumber, TravelDate, TicketCount, TotalPrice, Status) values ('deepak', 'BE-IXM-TRZ', '2025-12-04', 4, 10000,'Confirmed')"""
cur.execute(sql)

sql=f"""insert into {table_bookings} (Username, FlightNumber, TravelDate, TicketCount, TotalPrice, Status) values ('deepak', 'BE-IXM-MAA', '2025-11-25', 1, 6750,'Confirmed')"""
cur.execute(sql)

sql=f"""insert into {table_bookings} (Username, FlightNumber, TravelDate, TicketCount, TotalPrice, Status) values ('jacob', 'BE-MAA-SXV', '2025-09-25', 1, 5725,'Confirmed')"""
cur.execute(sql)

sql=f"""insert into {table_bookings} (Username, FlightNumber, TravelDate, TicketCount, TotalPrice, Status) values ('joanna', 'BE-CJB-IXM', '2025-11-02', 1, 5500,'Confirmed')"""
cur.execute(sql)


#commit all changes
con.commit()

#view table data
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

