import smtplib

EMAIL = "python.musin@gmail.com"
PASSWORD = "ffvjputzmmtqvokq"


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def send_email(self, message):
        self.server = smtplib.SMTP("smtp.gmail.com")
        self.server.ehlo()
        # Secure Connection
        self.server.starttls()
        # Log in
        self.server.login(user=EMAIL, password=PASSWORD)
        self.server.sendmail(from_addr=EMAIL, to_addrs="dan4ik377@gmail.com", msg=message)
        self.server.close()
        print("successfully sent the mail")
