import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("rameshwarsomvanshi17@gmail.com", "9834157393") 
# message to be sent 
message = "Website is not working. please check the code and push again ."
# sending the mail 
s.sendmail("rameshwar.somvanshi@gmail.com", "rameshwarsomvanshi17@gmail.com", message) 
# terminating the session 
s.quit()
