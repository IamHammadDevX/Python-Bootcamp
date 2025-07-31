import requests # pyright: ignore[reportMissingModuleSource]
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Weather API Setup ---
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "18f282a7433c98e212108a590075c67d"

weather_params = {
    "lat": 31.9744,
    "lon": 74.2244,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

forecast_slice = weather_data["list"][:4]
will_rain = False
rain_details = ""

for hour_data in forecast_slice:
    timestamp = hour_data["dt_txt"]
    condition_code = hour_data["weather"][0]["id"]
    description = hour_data["weather"][0]["description"]
    print(f"{timestamp} | {description} | Code: {condition_code}")

    if int(condition_code) < 700:
        will_rain = True
        rain_details += f"{timestamp}: {description}\n"

# --- Send Email Alert ---
if will_rain:
    print("It's going to rain today. Sending email alert ☔")

    # Email setup
    sender_email = "iamhammaddev03@gmail.com"        # 🔁 Replace with your Gmail
    app_password = "ymlzyrpqcahlkgan"  # 🔁 Replace with your Gmail App Password
    receiver_email = "iamhammaddev03@gmail.com"  # 🔁 Replace with where you want to send

    subject = "🌧 Rain Alert - Don't Forget Your Umbrella!"
    body = f"It's going to rain in the next 12 hours:\n\n{rain_details}\nStay dry! ☔"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Connect to Gmail SMTP server and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    print("✅ Email sent successfully!")
