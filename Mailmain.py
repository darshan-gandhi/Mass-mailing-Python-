import pandas as pd
import smtplib

#do not forget to turn on the Less secure app notification ON (Manage accounts->Security)
#enter your email ID and password to login
SenderAddress =""
password = ""

e = pd.read_excel("Emails.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Hello this is a try for automation testing"
subject = "Hey! Trial run!"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
