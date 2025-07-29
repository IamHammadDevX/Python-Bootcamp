import smtplib
import datetime as dt
import random


my_email = "iamhammaddev03@gmail.com"
my_password = "ymlzyrpqcahlkgan"

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 2:
    with open("31-Day32-AutomationEmail\\Birthday Wisher (Day 32) start\\quotes.txt") as quote_file:
        all_qoutes = quote_file.readlines()
        qoute_to_send = random.choice(all_qoutes)
    print(qoute_to_send)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
              to_addrs=my_email,
                msg=f"Subject: Regards Motivational Qoute \n\n{qoute_to_send}"
                )