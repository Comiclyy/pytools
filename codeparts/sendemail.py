import smtplib
import threading
import random
import string

def create_message(from_address, to_address, subject, body):
    """Create a MIME message object for sending an email"""
    from email.mime.text import MIMEText
    message = MIMEText(body)
    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = subject
    return message

def send_email(from_address, password, to_address, body, num_emails, num_threads):
    """Send a specified number of emails using a specified number of threads"""
    # set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_address, password)
    
    # define the email subject as 10 random ascii characters
    subject = ''.join(random.choices(string.ascii_letters, k=10))
    
    # send the emails using multiple threads
    for i in range(num_emails):
        thread_num = i % num_threads
        from_address_thread = from_address[thread_num]
        to_address_thread = to_address[i]
        message = create_message(from_address_thread, to_address_thread, subject, body)
        try:
            server.sendmail(from_address_thread, to_address_thread, message.as_string())
            print(f"Email {i+1} of {num_emails} sent using thread {thread_num+1} of {num_threads}")
        except Exception as e:
            print(f"Email {i+1} of {num_emails} failed to send using thread {thread_num+1} of {num_threads}")
            print(f"Error message: {str(e)}")
    server.quit()

# ask for user input
num_emails = int(input("How many emails do you want to send? "))
num_threads = int(input("How many threads do you want to use? "))
from_address = input("Enter your email address: ")
password = input("Enter your email password: ")
to_address = []
for i in range(num_emails):
    email = input(f"Enter the email address for email {i+1}: ")
    to_address.append(email)
body = input("Enter the email body: ")

# split the email addresses into multiple lists for threading
from_address = [from_address] * num_threads
to_address = [to_address[i::num_threads] for i in range(num_threads)]

# send the emails
threads = []
for i in range(num_threads):
    t = threading.Thread(target=send_email, args=(from_address[i], password, to_address[i], body, num_emails, num_threads))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()

print("All emails sent!")    
