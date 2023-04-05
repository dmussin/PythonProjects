import smtplib

EMAIL = "python.musin@gmail.com"
PASSWORD = "jpteqmshjmbfdkxv"


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def send_email(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure Connection
            connection.starttls()
            # Log in
            connection.login(user=EMAIL, password=PASSWORD)
            # print(f" emails ------ IN SEND EMAIL - NOTIFICATION MANAGER {emails}")
            for email in emails:
                # print(f" EMAIL IN SEND EMAIL - NOTIFICATION MANAGER ------  {email}")
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight! - from Python APP\n\n{message}\n{google_flight_link}".encode('utf-8')
                )

            print("successfully sent the mail")
