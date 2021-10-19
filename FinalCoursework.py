#! "C:\python3\python.exe"

import cgi, cgitb
cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()

import mysql.connector
conn = mysql.connector.connect(host='localhost',
                              database='skytravel',
                              user='root',
                              password='')
Dep = form.getvalue('Dep')
Des  = form.getvalue('Des')
Date = form.getvalue('trip-start')
Adults = form.getvalue('Adults')
Teens = form.getvalue('Teens')
Kids = form.getvalue('Kids')
Toddlers = form.getvalue('Toddlers')

dep=int(Dep)
des=int(Des)
Adult= int(Adults)
Teen=int(Teens)
Kid=int(Kids)
Toddler=int(Toddlers)

print("Content-type:text/html\n")
print('<html><head>')
print('<style>.divv{border: 5px groove royalblue;margin-top: 70px;margin-bottom: 100px;margin-right: 300px;margin-left: 250px;width:700px;text-align: justify;background-color: white;padding-left: 60px;width:500px;}</style>')
print('</head>')
print('<body style=" background-color:  #ffce8a;">')
print("<H1 style='color:white;border:10px groove royalblue;padding: 30px;background-color:#0546ad;text-align:center;'>Sky Travel Booking Portal</H1>")
#restrictions against errors
if dep==des:
    print("<H3 style='color:red;text-align:center;'>Error ! operation not possible</H3>")
    print('<br>')
    print('<a href="FinalCourswork.html">  Go back to the main page </a>')
    exit()

if Adult==0 and Teen==0 and Kid==0 and Toddler==0 :
    print("<H3 style='color:red;text-align:center;'><b>Error!</b> please enter the number of passengers </H3>")  
    print('<br>')
    print('<a href="FinalCourswork.html">  Go back to the main page </a>')
    exit()

if Adult==0 and Teen==0 : 
    print("<H3 style='color:red;text-align:center;'><b>Sorry!</b> under 12 years old are not allowed to travel alone </H3>")
    print('<br>')
    print('<a href="FinalCourswork.html">  Go back to the main page </a>')
    exit()
#retrieving data from the database
cursor = conn.cursor()    
if dep !=des:  
    
    
    cursor.execute("SELECT * FROM timetable WHERE Dep_ID = %s and Des_ID=%s"%(Dep,Des))
    rows=cursor.fetchall()
    if len(rows)>0 :
       cursor.execute("SELECT * FROM timetable WHERE Dep_ID= %s and Des_ID =%s and T_ID= 2"%(Dep,Des))
       lines=cursor.fetchall()
       if len(lines)>0 :
            print("<H3> Here are the flights available for the desired trip </H3>")
            for line in lines:
                cursor.execute("SELECT City_name from cities where City_ID=%s"%(Dep))
                result=cursor.fetchone()
                #transforming result to a list then to a string
                A=list(result)
                a=A[0]
                aa=str(a)
                print('<br>')
                print('<div class="divv">')
                print(" Departure city : <b>", aa,"</b>")
                print('<br>')

                cursor.execute("select City_name from cities where City_ID=%s" %(Des))
                Result=cursor.fetchone()

                B=list(Result)
                b=B[0]
                bb=str(b)
                print(" Destination city :<b>", bb,"</b>") 
                print('<br>')

                cursor.execute("SELECT Dep_Time FROM timetable WHERE Dep_ID=%s AND Des_ID=%s AND T_ID=2"%(Dep,Des))
                Time=cursor.fetchone()

                time=list(Time)
                t=time[0]
                T=str(t)
                print("Departure time : <b>",T,"</b>")
                print('<br>')

                cursor.execute("SELECT Arr_Time FROM timetable WHERE Dep_ID=%s AND Des_ID=%s AND T_ID=2"%(Dep,Des))
                Arrival=cursor.fetchone()

                Arr=list(Arrival)
                Ar=Arr[0]
                AR=str(Ar)
                print("Arrival time: <b>",AR,"</b>")
                print('<br>')
                print("Date of the trip : <b>%s</b> " %(Date))
                print('<br>')
                print("Number of Adults: <b>%d</b>" %(Adult))
                print('<br>')
                print("Number of Teens:<b>%d</b>" %(Teen))
                print('<br>')
                print("Number of Kids: <b>%d</b>" %(Kid))
                print('<br>')
                print("Number of Toddlers:<b>%d</b>" %(Toddler))

                cursor.execute("SELECT Cost_£ from timetable where Dep_ID=%s and Des_ID=%s and T_ID=2" %(Dep,Des))
                res=cursor.fetchone()
             #sum calculation
                RES=list(res)
                p=RES[0]
                x=p*Adult
                y=(p/2)*Teen
                z=(p/2)*Kid
                sum=x+y+z
                SUM=str(sum)
                print('<br>')
                print('Cost is<b style="color:red;">',sum,'£</b>')

                cursor.execute("SELECT ID FROM timetable where Dep_ID=%s and Des_ID=%s and T_ID=2" %(Dep,Des))
                ID=cursor.fetchone()
                id=list(ID)
                m=id[0]
                M=str(m)
                #sending  data to FinalCoursework2.py 
                print('<form action="FinalCoursework2.py" method="post">')
                print('<br><br>')
                print('<input type="hidden" id="ID" name="BookReference" value="'+M+'">')
                print('<input type="hidden" id="Dep" name="Dep" value="'+aa+'"> ')
                print('<input type="hidden" id="Des" name="Des" value="'+bb+'">')
                print('<input type="hidden" id="Date" name="trip-start" value="'+Date+'">')
                print('<input type="hidden" id="Adult" name="Adult" value="'+Adults+'">')
                print('<input type="hidden" id="Teen" name="Teen" value="'+Teens+'">')
                print('<input type="hidden" id="Kid" name="Kid" value="'+Kids+'">')
                print('<input type="hidden" id="Toddler" name="Toddler" value="'+Toddlers+'">')
                print('<input type="hidden" id="Dep_Time" name="Dep_Time" value="'+T+'">')
                print('<input type="hidden" id="Arr_Time" name="Arr_Time" value="'+AR+'">')
                print('<input type="hidden" id="Cost" name="Cost" value="'+SUM+'">')
                print('<input type="submit" value="Book" style=" background-color: #ffe4bf;">')
                print('</div>')
                print('</form>')
                
           
       else:
            print("<H3>There is no flight for this destination</H3>") 

       cursor.execute("SELECT * FROM timetable WHERE  Dep_ID=%s AND Des_ID=%s AND T_ID=1"%(Dep,Des))
       LINES=cursor.fetchall()
       if len(LINES)>0 :
           print("<H3>Here are the Buses  available for the desired trip</H3>")
           for LINE in LINES:
                cursor.execute("SELECT City_name from cities where City_ID=%s"%(Dep))
                city=cursor.fetchone()

                cit=list(city)
                ci=cit[0]
                c=str(ci)
                print('<br>')
                print('<div class="divv">')
                print("Departure city:<b>", c,"</b>")
                cursor.execute("select City_name from cities where City_ID=%s" %(Des))
                City=cursor.fetchone()

                Cit=list(City)
                Ci=Cit[0]
                C=str(Ci)
                print('<br>')
                print("Destination city: <b>", C,"</b>")  
                cursor.execute("SELECT Dep_Time FROM timetable WHERE Dep_ID=%s AND Des_ID=%s AND T_ID=1"%(Dep,Des))
                DTime=cursor.fetchone()

                dtime=list(DTime)
                w=dtime[0]
                W=str(w)
                print('<br>')
                print("Departure time:<b>",W,"</b>")

                cursor.execute("SELECT Arr_Time FROM timetable WHERE Dep_ID=%s AND Des_ID=%s AND T_ID=1"%(Dep,Des))
                ARRIVAL=cursor.fetchone()

                ARR=list(ARRIVAL)
                AR=ARR[0]
                H=str(AR)
                print('<br>')
                print("Arrival time: <b>",H,"</b>")
                print('<br>')
                print("Date of the trip: <b>%s</b> " %(Date))
                print('<br>')
                print("Number of Adults: <b>%d</b>" %(Adult))
                print('<br>')
                print("Number of Teens: <b>%d</b>" %(Teen))
                print('<br>')
                print("Number of Kids : <b>%d</b>" %(Kid))
                print('<br>')
                print("Number of Toddlers: <b>%d</b>" %(Toddler))
                cursor.execute("SELECT Cost_£ FROM timetable where Dep_ID=%s and Des_ID=%s and T_ID=1" %(Dep,Des))
                Cost=cursor.fetchone()

                #sum calculation
                COS=list(Cost)
                R=COS[0]
                s=R*Adult
                o=(R/2)*Teen
                n=(R/2)*Kid
                sum=s+o+n
                SUM=str(sum)
                print('<br>')
                print('Cost is: <b style="color:red;">',sum,'£</b>')

                cursor.execute("SELECT ID FROM timetable where Dep_ID=%s and Des_ID=%s and T_ID=1" %(Dep,Des))
                id=cursor.fetchone()
                Id=list(id)
                u=Id[0]
                U=str(u)
                #sending data to FinalCoursework2
                print('<form action="FinalCoursework2.py" method="post">')
                print('<br><br>')
                print('<input type="hidden" id="ID" name="BookReference" value="'+U+'">')
                print('<input type="hidden" id="Dep" name="Dep" value="'+c+'"> ')
                print('<input type="hidden" id="Des" name="Des" value="'+C+'">')
                print('<input type="hidden" id="Date" name="trip-start" value="'+Date+'">')
                print('<input type="hidden" id="Adult" name="Adult" value="'+Adults+'">')
                print('<input type="hidden" id="Teen" name="Teen" value="'+Teens+'">')
                print('<input type="hidden" id="Kid" name="Kid" value="'+Kids+'">')
                print('<input type="hidden" id="Toddler" name="Toddler" value="'+Toddlers+'">')
                print('<input type="hidden" id="Dep_Time" name="Dep_Time" value="'+W+'">')
                print('<input type="hidden" id="Arr_Time" name="Arr_Time" value="'+H+'">')
                print('<input type="hidden" id="Cost" name="Cost" value="'+SUM+'">')
                print('<input type="submit" value="Book" style=" background-color: #ffe4bf;">')
                print('</div>')
                print('</form>')
    
       else:
             print("<H3>there is no bus for this destination</H3>")
    else:
         print("<H2 style='color:red;'>This trip is not offered by our agency sorry!</H2>") 
 
cursor.close()
conn.close() 
print('</body>')
print('</html>')

















   

