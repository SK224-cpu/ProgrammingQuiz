from ReadCSV import CreateQuestion
import datetime
import smtplib, ssl
from configparser import ConfigParser
from email.message import EmailMessage

def Consolidated():
    #calling Q1
    readCSV_Coding_test ="data/csv_text_csv.csv"
    removeCSV_Coding_test = "data/RemovedQuestions/"
    question1=CreateQuestion(readCSV_Coding_test, removeCSV_Coding_test)

    #calling Q2
    readCSV_Concepts_test ="data/Programming_Test.csv"
    removeCSV_Concepts_test ="data/RemovedQuestions/programming_quiz.csv"
    question2=CreateQuestion(readCSV_Concepts_test, removeCSV_Concepts_test)

    #calling Q3
    readCSV_Quiz_test ="data/Coding_quiz.csv"
    removeCSV_Quiz_test ="data/RemovedQuestions/removed_coding_quiz.csv"
    question3 = CreateQuestion(readCSV_Quiz_test, removeCSV_Quiz_test)

    return (
    
    f"Today's {datetime.datetime.now().date()} question paper:\n"
    f"Q1. {question1}\n"
    f"Q2. {question2}\n"
    f"Q3. {question3}\n"
    "Good Luck!"
)

# s = smtplib.SMTP('smtp.gmail.com',587)
# s.starttls()
# s.login("sktest052025@gmail.com","admin123#")
# message =   Consolidated()
# s.sendmail("sktest052025@gmail.com","shrutikhonde412@gmail.com",message)
# s.quit()

# import smtplib, ssl
config = ConfigParser()
config.read('configuration.ini')
smtp_server = config['EMAIL']['smtp_server']
port = config['EMAIL']['port']
sender_email = config['EMAIL']['sender_email']
password = config['EMAIL']['password']

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    message =   Consolidated()
    msg = EmailMessage()
    msg['Subject'] = f"{datetime.datetime.now().date()} Quiz\n"
    msg['From'] = sender_email
    msg['To'] = "shrutikhonde412@gmail.com"
    msg.set_content(message)
    server.send_message(msg,"sktest052025@gmail.com","shrutikhonde412@gmail.com")
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()


