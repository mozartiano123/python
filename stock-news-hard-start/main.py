import requests
import os
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_api_query = "tesla"
news_api_key = "31733f1591d34517bb289888dc979a45"
stocks_api_key = "21IEKJSBDVAWD6JU"
STOCKS_API_INTERVAL = "60min"

news_api_parameters = {
    "q":news_api_query,
    "apiKey":news_api_key
}

stocks_api_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval":STOCKS_API_INTERVAL,
    "apikey": stocks_api_key
}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday
# then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday.
# Find the positive difference between the two prices. e.g. 40 - 20 = -20,
# but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
response_stocks = requests.get(STOCK_ENDPOINT, params=stocks_api_parameters)
response_stocks.raise_for_status
api_response = response_stocks.json()
stocks = api_response[f"Time Series ({STOCKS_API_INTERVAL})"]
closing_prices = [float(value["4. close"]) for key,value in stocks.items() if str(key).split()[1] == "20:00:00"]
price_diff_value = abs(closing_prices[0] - closing_prices[1])
price_diff_pct = round((price_diff_value/closing_prices[0])*100,2)



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
response_news = requests.get(NEWS_ENDPOINT, params=news_api_parameters)
response_news.raise_for_status
api_response = response_news.json()
articles = api_response["articles"]





## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = "ACbb4df1f4fe4e77265424a5f538942f4f"
auth_token = "05953cfbb9798ee508f45a6524c9672a"
client = Client(account_sid, auth_token)

if price_diff_pct >= 5:
    for item in articles[:3]:
        news_title = item["title"]
        news_desc = item["description"]
        body = f"{news_title} : {news_desc}"

        message = client.messages \
            .create(
            body= body,
            from_='+18312939811',
            to='+5511957789288'
        )
        print(message.sid)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

