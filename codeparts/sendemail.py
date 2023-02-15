import smtplib
import random
import string

# get the number of emails and threads to send and use
num_emails = int(input("How many emails do you want to send? "))
num_threads = int(input("How many threads do you want to use? "))

# get the email address to send the emails to
to_address = input("Enter the email address to send the emails to: ")

# get the body of the email
body = input("Enter the body of the email: ")

# generate a random subject for each email
def generate_subject():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))
# ask for the user's email and password login
email = input("Enter your email: ")
password = input("Enter your password: ")

# send the emails
for i in range(num_threads):
    for j in range(num_emails):
        subject = generate_subject()
        message = f"Subject: {subject}\n\n{body}"
        server = None  # initialize the server variable to None
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, to_address, message)
            print(f"Email {j+1} of {num_emails} sent successfully using thread {i+1} of {num_threads}")
        except:
            print(f"Email {j+1} of {num_emails} failed to send using thread {i+1} of {num_threads}")
        finally:
            if server is not None:  # check if server is not None before calling server.quit()
                server.quit()
