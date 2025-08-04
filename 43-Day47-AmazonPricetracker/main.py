import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


URL = "https://www.amazon.com/Apple-iPhone-256GB-Black-Titanium/dp/B0DMX8C67G/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

sender_email = "iamhammaddev03@gmail.com"
app_password = "ymlzyrpqcahlkgan"


response = requests.get(url=URL, headers=headers)
amazon_product_link = response.text
soup = BeautifulSoup(amazon_product_link, "lxml")
title = soup.title.string

price_tag = soup.find("span", class_="a-offscreen").getText()
price_without_currency = price_tag.split("$")[1]
price_cleaned = price_without_currency.replace(",", "")
price_as_float = float(price_cleaned)

target_price_i_phone = 1200

if price_as_float < target_price_i_phone:
    subject = "🔥 HOT DEAL: Your iPhone 16 Pro Max is Now Cheaper!"
    
    body = f"""
🚨 Limited Time Offer!

🎯 The **{title}** is now just **${price_as_float:.2f}** on Amazon — below your target price of ${target_price_i_phone}!

💡 Don’t miss out on this deal — prices can go up anytime!

🛒 Grab it now: {URL}

Happy shopping!
– Your Amazon Price Tracker Bot 🤖
""".strip()

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = sender_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, sender_email, msg.as_string())

    print(f"✅ Email sent! Deal Found for ${price_as_float:.2f}. Check your inbox 📬")
else:
    print(f"🔍 Current price ${price_as_float:.2f} is still above your target of ${target_price_i_phone}. No email sent.")
