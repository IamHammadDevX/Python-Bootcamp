import requests
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from translate import Translator

# Load environment variables
load_dotenv()

# Config
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# ENV Variables
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# Translator
translator = Translator(to_lang="en")

# --- 1. Get Stock Data ---
try:
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
except Exception as e:
    print(f"❌ Stock API error: {e}")
    exit()

data_list = [value for (key, value) in data.items()]
yesterday_closing = float(data_list[0]["4. close"])
day_before_closing = float(data_list[1]["4. close"])
difference = abs(yesterday_closing - day_before_closing)
up_down = "🔺" if yesterday_closing > day_before_closing else "🔻"
diff_percent = round((difference / yesterday_closing) * 100)

# --- 2. If change > 1%, Get News ---
if diff_percent > 1:
    try:
        news_params = {
            "apikey": NEWS_API_KEY,
            "qInTitle": COMPANY_NAME,
        }
        news_response = requests.get(NEWS_ENDPOINT, params=news_params)
        news_response.raise_for_status()
        articles = news_response.json()["articles"][:3]
    except Exception as e:
        print(f"❌ News API error: {e}")
        articles = []

    # Translate and format articles
    formatted_articles = []
    for article in articles:
        try:
            title = translator.translate(article['title'])
            description = translator.translate(article['description'])
        except Exception as e:
            print(f"⚠️ Translation error: {e}")
            title = article['title']
            description = article['description']

        message = f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {title}\nBrief: {description}"
        formatted_articles.append(message)

    # --- 3. Send Notifications via Email ---
    for message in formatted_articles:
        subject = f"{STOCK_NAME}: {up_down}{diff_percent}% Stock Alert"
        body = message

        try:
            msg = MIMEMultipart()
            msg["From"] = MY_EMAIL
            msg["To"] = MY_EMAIL
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(MY_EMAIL, MY_PASSWORD)
                server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string())
            print("✅ Email sent.")
        except Exception as e:
            print(f"❌ Email error: {e}")
