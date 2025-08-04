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



"""
# TELEGRAM_TOKEN = "8388531762:AAGbwo4-pgmSv9X3jnEI7QDLdYpr6w9n1x4"
# CHAT_ID = "7447515464"
# import requests
# from bs4 import BeautifulSoup
# import time

# URL = "https://www.amazon.com/Apple-iPhone-256GB-Black-Titanium/dp/B0DMX8C67G/"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://www.amazon.com/",
#     "DNT": "1"
# }

# def send_telegram_message(message):
#     telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
#     params = {
#         "chat_id": CHAT_ID,
#         "text": message,
#         "parse_mode": "Markdown"
#     }
#     response = requests.post(telegram_url, data=params)
#     return response.status_code == 200

# try:
#     response = requests.get(url=URL, headers=headers, timeout=10)
#     response.raise_for_status()
    
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Try different selectors for price
#     price_element = (soup.find("span", class_="a-offscreen") or 
#                     soup.find("span", class_="a-price-whole") or
#                     soup.find("span", {"data-a-color": "price"}))
    
#     if not price_element:
#         send_telegram_message("⚠️ Price element not found. Amazon may have changed their page structure.")
#         print("Could not find price element on the page")
#         exit()

#     title = soup.find("span", id="productTitle").get_text().strip() if soup.find("span", id="productTitle") else "iPhone 15 Pro Max"

#     price_text = price_element.get_text().strip()
#     price_without_currency = price_text.split("$")[-1]
#     price_cleaned = price_without_currency.replace(",", "").replace(" ", "")
#     price_as_float = float(price_cleaned)

#     target_price_i_phone = 1200

#     if price_as_float < target_price_i_phone:
#         message = f"""
# # 🔥 *PRICE ALERT!* 🔥

# # 📱 *{title}*
# # 💰 *Current Price:* ${price_as_float:.2f}
# # 🎯 *Your Target:* ${target_price_i_phone}

# # 🛒 [Buy Now]({URL})
# """
#         if send_telegram_message(message):
#             print(f"✅ Telegram alert sent! Price dropped to ${price_as_float:.2f}")
#         else:
#             print("Failed to send Telegram message")
#     else:
#         print(f"Current price ${price_as_float:.2f} is above target of ${target_price_i_phone}")

# except requests.exceptions.RequestException as e:
#     error_msg = f"❌ Error fetching Amazon page: {str(e)}"
#     print(error_msg)
#     send_telegram_message(error_msg)
# except Exception as e:
#     error_msg = f"❌ Unexpected error: {str(e)}"
#     print(error_msg)
#     send_telegram_message(error_msg)
# """