from pprint import pprint
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# gmail
EMAIL = "python.musin@gmail.com"
PASSWORD = "zhzzcbaoicbihxpu"
URL = "https://www.amazon.de/-/en/Cobear-Customisable-Leather-Non-Slip-Waterproof/dp/B0BKFQRJ9V/ref=psdc_79899031_t3_B0BLRTVTZV"


headers = {
    #"Accept-line": "sofman-4pyxfo-Vurdog",
    "Accept-Language": "en-GB,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()

amazon = response.text
# pprint(amazon)

# Beautiful soup
soup = BeautifulSoup(amazon, "lxml")
# pprint(soup)

price = soup.find(name="span", class_="a-offscreen").getText()
product_title = soup.find(name="span", class_="a-size-large product-title-word-break").getText().strip()
# print(product_title.strip())
# print(price.getText())

float_price = float(price.replace("€", ""))
print(float_price)

# Setting and sending the mail

message = f"Subject:Amazon Price Alert! \n\n " \
              f"{product_title} is now - {float_price} EUR." \
              f"\n\n {URL}" \
              f"\n\n This is a automated price alert that was sent using my Python app."

if float_price <= 110:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Secure Connection
        connection.starttls()
        #Log in
        connection.login(user=EMAIL, password=PASSWORD)
        # Send Email
        connection.sendmail(from_addr=EMAIL, to_addrs="dan4ik77@mail.ru", msg=message.encode('utf-8'))
        print("Email was sent successfully!")
else:
    print("Sorry price is still to high 🥲")