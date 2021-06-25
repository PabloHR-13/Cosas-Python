from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
mensaje = MIMEMultipart("plain")
mensaje["From"]="pruebraemail@gmail.com"
mensaje["Subject"] ="Correo de prueba desde Python 3"
adjunto = MIMEBase("application","octect-stream")
adjunto.set_payload(open("correo_prueba.txt","rb").read())
adjunto.add_header("content-Disposition",'attachment; filename="mensaje.txt"')
mensaje.attach(adjunto)
smtp = SMTP("smtp.gmail.com")
smtp.starttls()
smtp.login("pruebraemail@gmail.com","prueba123")
smtp.sendmail("pruebraemail@gmail.com","pruebraemail@gmail.com",mensaje.as_string())
smtp.quit()