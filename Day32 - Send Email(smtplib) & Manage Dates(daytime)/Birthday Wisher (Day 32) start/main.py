import smtplib
import datetime as dt
import random



now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 3:
    with open("quotes.txt") as quote:
        all_quotes = quote.readlines()
        randon_quote = random.choice(all_quotes)
        print(randon_quote)

    my_email = "python.musin@gmail.com"
    password = "ffvjputzmmtqvokq"
    message = f"Subject:Motivational Quotes on Mondays \n\n " \
              f"This is a random quote that was sent using my Python app to you." \
              f"\n\n Enjoy :)" \
              f"\n\n {randon_quote}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Secure Connection
        connection.starttls()
        #Log in
        connection.login(user=my_email, password=password)
        # Send Email
        connection.sendmail(from_addr=my_email, to_addrs="dan4ik77@mail.ru", msg=message.encode('utf-8'))
        connection.sendmail(from_addr=my_email, to_addrs="karina_idrisova@mail.ru", msg=message.encode('utf-8'))
        connection.sendmail(from_addr=my_email, to_addrs="ekaterinatsoy1@gmail.com ", msg=message.encode('utf-8'))