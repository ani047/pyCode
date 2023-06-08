import smtplib
server = smtplib.SMTP('smtp.gmail.com' , 465)
server.starttls()
server.login('anilmeran80@gmail.com','Arvi$098')
server.sendmail('anilmeran80@gmail.com','anilmeran14081999@gmail.com','mail sent')
print("mail sent")


# import smtplib

# server = smtplib.SMTP('smtp.gmail.com',587)

# server.starttls()

# server.login('anilmeran80@gmail.com','Arvi$098')

# server.sendmail('anilmeran80@gmail.com' , 'anilmeran14081999@gmail.com','Mail send')
# print("mail sent")