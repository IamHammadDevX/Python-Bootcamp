import smtplib


my_email = "iamhammaddev03@gmail.com"
my_password = "ymlzyrpqcahlkgan"

# for gmail
with smtplib.SMTP("smtp.gmail.com") as connection:
# for yahoo, hotmail, smtp.mail.yahoo.com, smtp.live.com respectively
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
                        from_addr=my_email,
                         to_addrs=my_email,
                           msg="Subject:Regards Python automation \n\nHello, Buddy how are you? this is the testing email from python automation."
                           )