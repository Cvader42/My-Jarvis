import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'your_email@gmail.com'  # Your email address
sender_password = 'your_password'      # Your email password
receiver_email = 'recipient@example.com'  # Recipient's email address

# Create a MIMEText object to represent the email content
email_subject = 'Hello from your Python script!'
email_body = 'This is the content of the email.\nYou can write your message here.'
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

