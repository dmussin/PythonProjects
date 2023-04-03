from flask import Flask
from flask import render_template, request
import smtplib


MY_EMAIL = "python.musin@gmail.com"
PASSWORD = "GOOGLE APP PW"

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Secure Connection
        connection.starttls()
        # Log in
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # Send Email
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs='dan4ik77@mail.ru',
                            msg=email_message
                            )


# @app.route("/form-entry", methods=["GET", "POST"])
# def receive_data():
#     data = request.form
#     print(data["name"])
#     print(data["email"])
#     print(data["phone"])
#     print(data["message"])
#     return "<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run(debug=True)
