##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
from datetime import datetime
import random
import pandas

MY_EMAIL = "python.musin@gmail.com"
PASSOWORD = "ffvjputzmmtqvokq"

# Todays day and month in tuple
today = datetime.now()
today_tuple = (today.month, today.day)

# Pandas to read the CSV
data = pandas.read_csv("birthdays.csv")

# Dict comprehension
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today is matches a birthday in the birthdays.csv
if (today_tuple) in birthdays_dict:
    # Holding a row of data
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # Read the text from the file
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Secure Connection
        connection.starttls()
        #Log in
        connection.login(user=MY_EMAIL, password=PASSOWORD)
        # Send Email
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday Bitch!!! \n\n{contents}"
                                f"\n\n This is a random message that was sent using my Python app to you."
                            )




