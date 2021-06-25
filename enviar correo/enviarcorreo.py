from email import message
import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('pruebraemail@gmail.com','prueba123')
subject = input('Introduce el asunto: ')
message = input('Introduce el mensaje: ')
message = 'Subject: {}\n\n{}'.format(subject, message)
server.sendmail('pruebraemail@gmail.com', 'pruebraemail@gmail.com', message)
server.quit()
print('se envio correctamente')