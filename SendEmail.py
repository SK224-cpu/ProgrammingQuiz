import smtplib, ssl
from configparser import ConfigParser
from email.message import EmailMessage

def SendEmail(richTextMessage, fallbackMessage, reciversEmailId):
    config = ConfigParser()
    config.read('configuration/configuration.ini')
    smtp_server = config['EMAIL']['smtp_server']
    port = config['EMAIL']['port']
    login = config['EMAIL']['login']
    password = config['EMAIL']['password']
    sender_email = config['EMAIL']['sender_email']

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls(context=context) # Secure the connection
            server.login(login, password)
            message =  richTextMessage
            msg = EmailMessage() 
            msg['Subject'] = "Ready to Code? Your Programming Quiz Awaits 🚀"
            msg['From'] = sender_email
            msg['To'] = reciversEmailId
            msg.set_content(fallbackMessage)
            msg.add_alternative(richTextMessage, subtype='html')
            server.send_message(msg,sender_email,reciversEmailId)
    except Exception as e:
        print(e)