import smtplib
from email.message import EmailMessage
import os


API_KEY = os.getenv("API_KEY")
email_address = os.getenv("email")
email_pw = os.getenv("email_pw")

msg = EmailMessage()
msg["Subject"] = "--Alert! Whale has sold--"
msg["From"] = "jmclark3592@gmail.com"
msg["To"] = email_address
msg.set_content("Whale has sold! Consider dumping your position.")

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # outgoing
server.login(email_address, email_pw)
server.send_message(msg)
server.quit()
