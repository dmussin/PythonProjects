# import smtplib
#
# my_email = "python.musin@gmail.com"
# password = "ffvjputzmmtqvokq"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Secure Connection
#     connection.starttls()
#     #Log in
#     connection.login(user=my_email, password=password)
#     # Send Email
#     connection.sendmail(from_addr=my_email, to_addrs="dan4ik77@mail.ru",
#                         msg="Subject:Test Email \n\n Hello Test Email")


import datetime as dt


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=1991, month=7, day=13)
print(day_of_week)