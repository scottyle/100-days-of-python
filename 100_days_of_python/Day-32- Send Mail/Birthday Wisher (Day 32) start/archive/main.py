import smtplib
import datetime as dt

my_email = "@gmail.com"
password = ""

with smtplib.SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="@gmail.com",
        msg="Subject:Hello\n\nThis is the body of the email.")

current_time = dt.datetime.now() 
year = current_time.year
month = current_time.month
day_of_week = current_time.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995,month=12,day=15,hour=4)
print(date_of_birth)
