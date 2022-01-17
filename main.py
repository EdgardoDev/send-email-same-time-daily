from dotenv import load_dotenv
import yagmail
import os
import time
from datetime import datetime as dtime

load_dotenv()

# Create initial variables.
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")

# Email subject.
email_subject = "Hello from Python! 👋"

# Email body.
email_body = """
Hello! 
This is the body content of the email.
Best regards,
The Python Script. 🤖
"""
while True:
  now = dtime.now()
  # If the time now is 15:15 run the rest.
  if now.hour == 15 and now.minute == 15:
    # Create an SMTP object instance
    smtp = yagmail.SMTP(user=sender_email, password=os.getenv("APP_PASSWORD"))
    # Send email.
    smtp.send(to=receiver_email, subject=email_subject, contents=email_body)
    print("📬 The Email Was Successfully Sent!")
    # Add a time interval, after one hour the script will check if the 
    # conditions if the if statement are met.
    time.sleep(3600)