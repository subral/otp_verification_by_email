import smtplib
import random
otp = random.randint(100000, 999999)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sender_email.com','App_password')
msg = "Hello your otp is here \n " + str(otp)
server.sendmail('sender_mail.com','reciver_mail.com', msg)
server.quit()
