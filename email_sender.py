import sys
import smtplib
from email.message import EmailMessage
from email.utils import formataddr

receiver_email_id = ""
receiver_email_password = ""

sender_name = ""
sender_email_id = ""

def send_email(email_body):
    body = email_body
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
        server.ehlo()
        server.login(receiver_email_id, receiver_email_password)
        
        msg = EmailMessage()
        msg['Subject'] = ""
        msg['From'] = formataddr((sender_name , sender_email_id))
        msg.set_content(body)
        msg['To'] = receiver_email_id
        
        try:
            server.send_message(msg)
        except Exception as e:
            server.quit()

    except Exception as e:
        print ("Something went wrong")

    finally:
        print ("Shutting down the server")
        server.quit()

sys.exit()
