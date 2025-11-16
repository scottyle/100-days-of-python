import smtplib

my_email = "scottyle02-test@gmail.com"
password = "jzwv ypon kbxj wruk"

connection = smtplib.SMTP(host="smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="scottyle02@gmail.com",msg="Hello")
connection.close()