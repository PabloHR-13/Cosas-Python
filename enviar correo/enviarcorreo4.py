from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from smtplib import SMTP
mensaje = MIMEMultipart("plain")
mensaje["Subject"] = input("Introduzca el asunto: ")
message = input("Introduzca el mensaje: ")
message = MIMEText(message, 'plain')
mensaje.attach(message)

archivo = str(input("¿Desea enviar un archivo? (SI/NO): "))

if archivo.upper() == 'SI':
    ruta = input("Introduzca la ruta con el archivo que va a adjuntar (Introduce la ruta absoluta): ")
    adjunto = MIMEBase("application","octect-stream")
    adjunto.set_payload(open(ruta,"rb").read())
    #adjunto.set_payload(open("correo_prueba.txt","rb").read())
    edita = str(input("¿Desea cambiar el nombre del archivo?: (SI/NO): "))

    if edita.upper() == 'SI':
        nombre = input("Introduce el nombre del archivo que se va a adjuntar: ")
        #adjunto.add_header("content-Disposition",'attachment; filename="mensaje.txt"')
        adjunto.add_header("content-Disposition",'attachment; filename={}' .format(nombre))
        mensaje.attach(adjunto)
    else:
        nombre_defecto = "mensaje.txt"
        adjunto.add_header("content-Disposition",'attachment; filename={}' .format(nombre_defecto))
        mensaje.attach(adjunto)
    smtp = SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login("pruebraemail@gmail.com","prueba123")
    smtp.sendmail("pruebraemail@gmail.com","pruebraemail@gmail.com",mensaje.as_string())
    smtp.quit()
else:
    smtp = SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login("pruebraemail@gmail.com","prueba123")
    smtp.sendmail("pruebraemail@gmail.com","pruebraemail@gmail.com",mensaje.as_string())
    smtp.quit()