import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email, sender_password, receiver_email, email_subject, email_body):
    """
    Send an email.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        receiver_email (str): The recipient's email address.
        email_subject (str): The email subject.
        email_body (str): The email body.
    """

    # Create a MIMEText object to represent the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = email_subject
    message.attach(MIMEText(email_body, 'plain'))

    # Connect to the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Use 465 for SSL connection
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure one
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('Email sent successfully!')
    
    except Exception as e:
        print('An error occurred:', str(e))

    finally:
        server.quit()  # Close the connection to the server

