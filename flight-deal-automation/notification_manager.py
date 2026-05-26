import smtplib
import os
from dotenv import load_dotenv

load_dotenv() # Helps load environment variables



class NotificationManager:#This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.email = os.getenv("YOUR_EMAIL")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.recipient = os.getenv("RECIPIENT_EMAIL")

        print("EMAIL LOADED:", self.email)


    def send_email(self, message, recipient_email):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)

            connection.sendmail(from_addr= self.email,to_addrs=recipient_email,msg= f"Subject:Flight Price Alert!\n\n{message}")

