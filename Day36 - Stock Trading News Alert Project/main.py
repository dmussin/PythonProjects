import requests
from twilio.rest import Client

# NEWS API KEY
NEWS_API_KEY = "394d4e8a885747f281ad9fcc316c5ccb"

# CoinMarketCap API KEY
COIN_API_KEY = "3977761b-4265-4731-8882-24981f978f69"

# Twilio creds
account_sid = "AC2773e572f6feb9470c4e9a7eddf05007"
auth_token = "49e8c717470f70165646e58dd8597cc8"




# News request
def news_request():
    response = requests.get(url=f"https://newsapi.org/v2/everything?q=bitcoin&sortBy=popularity&apiKey={NEWS_API_KEY}")
    response.raise_for_status()

    # Request about the Bitcoin
    bitcoin_news = response.json()

    # bitcoin_articles = bitcoin_news["articles"]

    # bitcoin_articles = bitcoin_news["articles"][0]["title"]
    # bitcoin_url = bitcoin_news["articles"][0]["url"]
    # print(f"{bitcoin_article} \n{bitcoin_url}")


    # three_articles = bitcoin_articles[:3]

    # Creating a new list with 3 articles info
    # formatted_articles = [f"Headline: {article['title']}.\nURL: {article['url']}" for article in three_articles]

    formatted_articles = f"{bitcoin_news['articles'][0]['title']} \n{bitcoin_news['articles'][0]['url']} " \
                         f"\n\n{bitcoin_news['articles'][1]['title']} \n{bitcoin_news['articles'][1]['url']} "\
                         f"\n\n{bitcoin_news['articles'][2]['title']} \n{bitcoin_news['articles'][2]['url']}"

    return formatted_articles

# Header param for CoinMarketCap
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COIN_API_KEY,
}

# CoinMarketCap Request
new_response = requests.get(url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC&convert=USD",
                            headers=headers)
new_response.raise_for_status()
coinmarket = new_response.json()
# print(coinmarket)

bitcoin_percent_change = coinmarket['data']['BTC']['quote']['USD']['percent_change_24h']
bitcoin_percentage = round(bitcoin_percent_change, 3)
bitcoin_price = coinmarket['data']['BTC']['quote']['USD']['price']

# Emoji
up_down = None
if bitcoin_percent_change > 3:
    up_down = "🔺"
else:
    up_down = "🔻"

print(f"The current price of Bitcoin is ${bitcoin_price}")
print(f"The current price change of Bitcoin in % is {bitcoin_percentage}")

if bitcoin_percent_change > 0 or bitcoin_percent_change < 0:
   article_for_sms = news_request()
   print(article_for_sms)

# ---- TURNED OFF ----

# Twilio Client
# client = Client(account_sid, auth_token)
# # message = client.messages.create(
#     body=f"BTC: {up_down}{bitcoin_percentage}\n{article_for_sms}",
#     from_="+16089797209",
#     to="+420776427177"
# )
#
# print(message.status)