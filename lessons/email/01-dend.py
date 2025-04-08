import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def connect_to_smtp(smtp_server, smtp_port, sender_email, sender_password):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        return server
    except Exception as e:
        print(f"Failed to connect to SMTP server: {e}")
        return None
    

def add_recipients(msg, all_recipients, cc_emails=None, bcc_emails=None):
  if cc_emails:
      msg['CC'] = ", ".join(cc_emails)
      all_recipients += cc_emails

  if bcc_emails:
      all_recipients += bcc_emails

  return all_recipients


def add_message(msg, body_text, body_html):
    if body_text:
        msg.attach(MIMEText(body_text, 'plain'))
    if body_html:
        msg.attach(MIMEText(body_html, 'html'))


def add_attachments(msg, attachments):
    if attachments:
        for file_path in attachments:
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    part = MIMEApplication(f.read())
                part.add_header('Content-Disposition', 'attachment',
                                filename=os.path.basename(file_path))
                msg.attach(part)


def send_email(
    server,
    sender_email,
    to_emails,
    subject="",
    body_text="",
    body_html=None,
    cc_emails=None,
    bcc_emails=None,
    attachments=None
):
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    all_recipients = list(to_emails)
    all_recipients = add_recipients(msg, all_recipients, cc_emails, bcc_emails)
    add_message(msg, body_text, body_html)
    add_attachments(msg, attachments)

    try:
        server.sendmail(sender_email, all_recipients, msg.as_string())
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

if __name__ == "__main__":
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    server = connect_to_smtp(smtp_server, smtp_port, sender_email, sender_password)

    send_email(
        server=server,
        sender_email=sender_email,
        to_emails=["recipient@example.com"],
        subject="Test Email with Attachments",
        body_text="This is a test email with attachments.",
        body_html="<html><body><h1>Test Email</h1><p>This is a <b>test email</b>.</p></body></html>",
        cc_emails=["cc_recipient@example.com"],
        bcc_emails=["bcc_recipient@example.com"],
        attachments=["path/to/your/file.pdf"]
    )
    
    server.quit()
