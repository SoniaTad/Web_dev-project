#! "C:\python3\python.exe"

import cgi, cgitb
cgitb.enable()
import random
form = cgi.FieldStorage()
print("Content-type:text/html\n")
print('<html><head>')
Reference=form.getvalue("BookReference")
Dep=form.getvalue("Dep")
Des=form.getvalue("Des")
Adults=form.getvalue("Adult")
Teens=form.getvalue("Teen")
Kids=form.getvalue("Kid")
Toddlers=form.getvalue("Toddler")
Date = form.getvalue('trip-start')
Dep_Time= form.getvalue('Dep_Time')
Arr_Time = form.getvalue('Arr_Time')
Cost= form.getvalue('Cost')
print('<style>.divv{border: 5px groove royalblue;margin-top: 70px;margin-bottom: 100px;margin-right: 300px;margin-left: 250px;width:700px;text-align: justify;background-color: white;padding-left: 60px;width:500px;}</style>')
print('</head>')
n = random.randint(10000,20000)
print('<body style="background-color: #ffce8a;">')
print("<H1 style='color:white;border:10px groove royalblue;padding: 30px;background-color:#0546ad;text-align:center;'>Sky Travel Booking Portal</H1>")
print('<H2>Your Receipt :</H2>')
print('<div class="divv">')
print('<p style="text-align:left;color:royalblue;font-size:18px;"><b>ST Booking Portal</b></p>')
print('<br>')
print('Booking number :')
print ('<b>',n,'</b>')
print('<br><br>')
print("Reference number <b>:%s</b>" %(Reference))
print('<br><br>')
print("Departure city <b>:%s</b>" %(Dep))
print('<br><br>')
print("Destination city <b>:%s</b>" %(Des))
print('<br><br>')
print("Date of the travel  <b>:%s</b>" %(Date))
print('<br><br>')
print("Departure Time  <b>:%s</b>" %(Dep_Time))
print('<br><br>')
print("Arrival Time <b>:%s</b>" %(Arr_Time))
print('<br><br>')
print(" Number of Adults <b>:%s</b>" %(Adults))
print('<br><br>')
print(" Number of Teens <b>:%s</b>" %(Teens))
print('<br><br>')
print(" Number of Kids  <b>:%s</b>" %(Kids))
print('<br><br>')
print(" Number of Toddler <b>:%s</b>" %(Toddlers))
print('<br><br>')
print("The Cost for this trip is<b style='color:red;'>:%s £</b>" %(Cost))
print('<br><br>')
print('</div>')
print('<H2>Please select the payment method you would like to use :</H2>')
print('<br><br>')
print('<input type="button" value="PayPal" style="color:blue;background-color:#42cef5;">')
print('<br><br>')
print('<input type="button" value="VisaCard" style="color:royalblue;background-color:yellow;">')
print('<br><br>')
print('<input type="button" value="MasterCard" style="color:white;background-color:red;">')
print('</body>')
print('</html>')