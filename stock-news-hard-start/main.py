import requests
import smtplib
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

me_email = "mnakhtar81@gmail.com"
passwd = "ujtf cyxf wijr krkp"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_price_api = "5MHRDWCY4C72JSUC"
news_api_key = "8c2ce530d1724a1e8dff110aa529daaf"

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_price_api
}

news_param = {
    "q": STOCK,
    "from": "2025-08-13",
    "to": "2025-08-13",
    "sortBy": "popularity",
    "apiKey": news_api_key
}

stock_connection = requests.get(url=STOCK_ENDPOINT, params=stock_param)
stock_connection.raise_for_status()
stock_data = stock_connection.json()
stock_price = stock_data["Time Series (Daily)"]
print(stock_price)
data_list = [value for (key,value) in stock_price.items()]

news_connection = requests.get(url=NEWS_ENDPOINT, params=news_param)
news_connection.raise_for_status()
stock_news = news_connection.json()["articles"]


#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday_closing_price = float(data_list[0]["4. close"])
# print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = float(data_list[6]["4. close"])
# print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
# print(difference)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_perc = (difference/yesterday_closing_price) * 100
# print(diff_perc)

#If TODO4 percentage is greater than 5 then print("Get News").
top_3_articles = stock_news[:3]
print(top_3_articles)
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#Create a new list of the first 3 article's headline and description using list comprehension.
articles = [f"Headlines: {article['title']}. \nBrief: {article['description']}" for article in top_3_articles]

#Send each article as a separate message via Twilio.
cnnct =smtplib.SMTP("smtp.gmail.com")
cnnct.starttls()
cnnct.login(user=me_email, password=passwd)
cnnct.sendmail(
    from_addr=me_email,
    to_addrs=me_email,
    msg=f"Subject: {STOCK}:\n\n{articles}"
)


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

