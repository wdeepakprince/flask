import mysql.connector as mysql
from flask import Flask,render_template,request,redirect, url_for, flash, session
from modules.credentials import * # local module file

app=Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flashing messages

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/Home")
def home():
    
    return render_template("home.html")

@app.route("/Signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route("/CreateAccount", methods=['GET', 'POST'])
def createaccount():
    if(request.method=='POST'):
        fname=request.form['fullname']
        uname=request.form['usrname']
        pwd=request.form['passwd']
        mail=request.form['emailID']

        blank=0
        if not fname:
            flash("Please enter the Full Name!", "error")
            blank=1
        if not uname:
            flash("Please enter the Username!", "error")
            blank=1
        if not pwd:
            flash("Please enter the Password!", "error")
            blank=1
        if not mail:
            flash("Please enter the Email ID!", "error")
            blank=1

        if blank:
            return render_template("signup.html")
        else:
            con=mysql.connect(host=host,user=username,password=password,database=database,charset=charset)
            cursor=con.cursor()
            val=(uname,pwd,fname,mail)
            cursor.execute("insert into user(Username,Password,FullName,EMail)values(%s,%s,%s,%s)",val)
            con.commit()
            cursor.close()
            con.close()
            return render_template("accountcreated.html")


@app.route("/ValidateLogin", methods=['GET', 'POST'])
def validatelogin():
    if(request.method=='POST'):
        
        uname=request.form['uname']
        pwd=request.form['pwd']
        if not uname:
            flash("Please enter the Username!", "error")
        if not pwd:
            flash("Please enter the Password!", "error")

        con=mysql.connect(host=host,user=username,password=password,database=database,charset=charset)        
        cursor=con.cursor()

        cursor.execute("SELECT 1 FROM "+table_user+" WHERE Username = '"+uname+"' LIMIT 1;")
        query_result=cursor.fetchall()
        if(query_result):
            print("User Exists!")
            cursor.execute("SELECT Password FROM "+table_user+" WHERE Username = '"+uname+"'")
            query_result=cursor.fetchall()
            if(query_result[0][0]==pwd):
                print("User authenticated successfully!")
                return redirect(url_for('dashboard',usernm=uname)) # Redirects to the dashboard
            else:
                print("Please enter the correct Password!")
                flash("Please enter the correct Password!", "error")
                return redirect(url_for('home'))
                
            
        else:
            print("User does NOT Exist")
            flash("User does NOT Exist!", "error")
            return redirect(url_for('home'))
            
        
        
        cursor.close()
        con.close()
        return render_template("dashboard.html")        
         
    
    return render_template("dashboard.html")


@app.route("/Dashboard/<usernm>", methods=['GET', 'POST'])
def dashboard(usernm):
    print(usernm)

    con=mysql.connect(host=host,user=username,password=password,database=database,charset=charset)        
    cursor=con.cursor()

    cursor.execute("SELECT * FROM "+table_flights)
    flight_query_result=cursor.fetchall()
    print(flight_query_result)
    
    cursor.execute("SELECT BookingID, FlightNumber, TravelDate, TicketCount, TotalPrice, Status FROM "+table_bookings+" WHERE Username='"+usernm+"'")
    booking_query_result=cursor.fetchall()
    print(booking_query_result)

    cursor.execute("SELECT FullName FROM "+table_user+" WHERE Username='"+usernm+"'")
    dashboarduserfullname=cursor.fetchall()
    print(dashboarduserfullname)
    
    cursor.close()
    con.close()
    return render_template("dashboard.html", dashboarduser=usernm,dashboardfname=dashboarduserfullname[0][0],flightdata=flight_query_result, bookingdata=booking_query_result)


@app.route("/Profile/<profileuser>", methods=['GET', 'POST'])
def profile(profileuser):
    print(profileuser)

    con=mysql.connect(host=host,user=username,password=password,database=database,charset=charset)        
    cursor=con.cursor()

    cursor.execute("SELECT * FROM "+table_user+" WHERE Username='"+profileuser+"'")
    profile_query_result=cursor.fetchall()
    print(profile_query_result)
    
    cursor.close()
    con.close()
    return render_template("profile.html", profiledata=profile_query_result)


@app.route("/EditProfile/<editprofileuser>", methods=['GET', 'POST'])
def editprofile(editprofileuser):
    print(editprofileuser)
    print("Edit Profile")
    editfname=request.form['fullname']
    '''uname=request.form['usrname']'''
    editpwd=request.form['passwd']
    editemailID=request.form['emailID']

    print(editfname)
    print(editpwd)
    print(editemailID)

    con=mysql.connect(host=host,user=username,password=password,database=database,charset=charset)        
    cursor=con.cursor()

    cursor.execute("UPDATE "+table_user+" SET Password='"+editpwd+"', FullName='"+editfname+"', EMail='"+editemailID+"' WHERE Username='"+editprofileuser+"'")
    con.commit()

    cursor.execute("SELECT * FROM "+table_user+" WHERE Username='"+editprofileuser+"'")
    updatedprofile_query_result=cursor.fetchall()
    print(updatedprofile_query_result)

    flash("Profile updated successfully!", "success")
    
    cursor.close()
    con.close()
    return render_template("profile.html", profiledata=updatedprofile_query_result)


@app.route("/DeleteProfile/<deleteprofileuser>", methods=['GET', 'POST'])
def deleteprofile(deleteprofileuser):
    print(deleteprofileuser)
    print("Delete Profile")

    con=mysql.connect(host=host,user=username,password=password,database=database,charset=charset)        
    cursor=con.cursor()

    cursor.execute("SELECT * FROM "+table_user+" WHERE Username='"+deleteprofileuser+"'")
    deleteprofile_query_result=cursor.fetchall()
    print(deleteprofile_query_result)

    cursor.close()
    con.close()
    return render_template("deleteaccount.html", delprofiledata=deleteprofile_query_result)

@app.route("/AccountDeleted/<deletedprofileuser>", methods=['GET', 'POST'])
def accountdeleted(deletedprofileuser):
    print(deletedprofileuser)
    print("Parked for Deletion")
    con=mysql.connect(host=host,user=username,password=password,database=database,charset=charset)        
    cursor=con.cursor()

    cursor.execute("DELETE FROM "+table_user+" WHERE Username='"+deletedprofileuser+"'")
    con.commit()
    print("Account Deleted")
    
    cursor.close()
    con.close()
    return render_template("deletionsuccess.html")

@app.route("/Booking/<bookinguser>/FlightID/<flightid>", methods=['GET', 'POST'])
def booking(bookinguser,flightid):
    print("Entering Booking")
    
    con=mysql.connect(host=host,user=username,password=password,database=database,charset=charset)        
    cursor=con.cursor()

    cursor.execute("SELECT FullName FROM "+table_user+" WHERE Username='"+bookinguser+"'")
    bookinguserfullname=cursor.fetchall()
    print(bookinguserfullname)

    cursor.execute("SELECT * FROM "+table_flights+" WHERE FlightNumber='"+flightid+"'")
    bookflight_query_result=cursor.fetchall()
    print(bookflight_query_result)
    
    cursor.close()
    con.close()
    return render_template("booking.html", dashboarduser=bookinguser,dashboardfname=bookinguserfullname[0][0],flightiddata=bookflight_query_result)

@app.route("/Booking/<bookinguser>/FlightID/<flightid>/Success", methods=['GET', 'POST'])
def bookingsuccess(bookinguser,flightid):
    print("Entering Booking Success")
    booktraveldate=request.form['booktraveldate']
    bookticketcount=request.form['bookpassengercount']
    print(booktraveldate)
    print(bookticketcount)
    
    con=mysql.connect(host=host,user=username,password=password,database=database,charset=charset)        
    cursor=con.cursor()

    cursor.execute("SELECT TicketCost FROM "+table_flights+" WHERE FlightNumber='"+flightid+"'")
    ticketcost_query_result=cursor.fetchall()
    print(ticketcost_query_result)
    print(ticketcost_query_result[0])
    print(ticketcost_query_result[0][0])

    ticketcost=ticketcost_query_result[0][0]
    print(ticketcost)

    print(type(bookticketcount))
    print(type(ticketcost))
    
    booktotalprice_int=int(bookticketcount)*ticketcost
    booktotalprice=str(booktotalprice_int)
    print("Total Price: ",booktotalprice_int)
    
    print(bookinguser)
    print(flightid)


    cursor.execute("SELECT FullName FROM "+table_user+" WHERE Username='"+bookinguser+"'")
    bookinguserfullname=cursor.fetchall()
    print(bookinguserfullname)

    cursor.execute("SELECT * FROM "+table_flights+" WHERE FlightNumber='"+flightid+"'")
    bookflight_query_result=cursor.fetchall()
    print(bookflight_query_result)
    
    cursor.execute("INSERT INTO "+table_bookings+" (Username, FlightNumber, TravelDate, TicketCount, TotalPrice, Status) values ('"+bookinguser+"', '"+flightid+"', '"+booktraveldate+"', "+bookticketcount+", "+booktotalprice+", 'Confirmed')")

    con.commit()
                   
    flash("Booking confirmed successfully!", "success")

    cursor.close()
    con.close()
    return render_template("booking.html", dashboarduser=bookinguser,dashboardfname=bookinguserfullname[0][0],flightiddata=bookflight_query_result)

    
if __name__=='__main__':
    app.run()
    


