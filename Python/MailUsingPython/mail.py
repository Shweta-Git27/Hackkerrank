import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("shweta.pandey@sakec.ac.in","your password")
subject="sending mail using python"
body="hii,shweta here...."
message="subject:{}\n\n {}".format(subject,body)
#print (message)
listofaddress=["shwetapandey2707@gmail.com","akhilesh.gupta@sakec.ac.in"]

ob.sendmail("shweta pandey",listofaddress,message)
print("send successfully")
ob.quit()