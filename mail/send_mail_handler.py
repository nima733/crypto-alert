import smtplib
from config import EMAIL_SENDER, roles
from email.message import EmailMessage

from localconfig import APP_PASSWORD


def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['from'] = EMAIL_SENDER
    msg['to'] = roles['body_email']['receiver']

    with smtplib.SMTP('smtp.gmail.com', 587) as email_server:
        email_server.starttls()
        email_server.login(EMAIL_SENDER, APP_PASSWORD)
        email_server.sendmail(msg['from'], msg['to'], msg.as_string())
