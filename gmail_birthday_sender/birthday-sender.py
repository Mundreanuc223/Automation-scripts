import smtplib
from email.mime.text import MIMEText


def happy_birthday(sender_email, recipient_email, password, recipient_name, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)  # creates a secure server to relay email to Gmail
    server.starttls()
    server.login(sender_email, password)  # logs into the user's Gmail

    message = MIMEText(message)   # creates an email message object and passes in the email content
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = f"Happy Birthday {recipient_name}!"

    server.sendmail(sender_email, recipient_email, message.as_string())   # sends the email
    server.quit()

if __name__ == '__main__':

    sender_email = "bigshaq22322@gmail.com"
    recipiant_email = "cmundreanu22@gmail.com"
    password = "wbgf kfcy miai klcr"   # enter a secure app password created in your Google settings
    recipiant_name = "Christian"
    message = "Happy Birthday Christian! I hope you have an amazing day and get to eat a lot of cake!"

    happy_birthday(sender_email, recipiant_email, password, recipiant_name, message)