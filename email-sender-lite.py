import smtplib, ssl
#import getpass

port  = 465
email = input(" Enter your email address: ")
password = input(" Enter your password: ")
#getpass.getpass(" Enter your password: ",password)
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
	server.login(email,password)
	print("\n Successfully logged in!")
	print("\n --------------------------------------")
	print("\n From: " + email)
	receiver_email = input(" To: ")
	subject = input("\n Subject: ")
	message = input("\n Message: ")
	message = "Subject: " + subject + "\n\n" + message
	server.sendmail(email,receiver_email,message)
	server.quit()
	print("\n --------------------------------------")
	print("\n Your email was sent !")
