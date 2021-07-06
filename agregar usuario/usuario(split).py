import imaplib
import email
from email.header import decode_header
import os
from getpass import getpass
from pyad import *
# Datos del usuario
username = input("Correo: ")
password = getpass("Password: ")

# Crear conexión
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# iniciar sesión
imap.login(username, password)

status, mensajes = imap.select("INBOX")
# print(mensajes)
# mensajes a recibir
N = 1
# cantidad total de correos
mensajes = int(mensajes[0])

for i in range(mensajes, mensajes - N, -1):
    # print(f"vamos por el mensaje: {i}")
#     # Obtener el mensaje
    try:
        res, mensaje = imap.fetch(str(i), "(RFC822)")
    except:
        break
    for respuesta in mensaje:
        if isinstance(respuesta, tuple):
            # Obtener el contenido
            mensaje = email.message_from_bytes(respuesta[1])
            # decodificar el contenido
            subject = decode_header(mensaje["Subject"])[0][0]
            if isinstance(subject, bytes):
                # convertir a string
                subject = subject.decode()
            # de donde viene el correo
            from_ = mensaje.get("From")
            print("Subject:", subject)
            print("From:", from_)
            print("Mensaje obtenido con exito")
            # si el correo es html
            if mensaje.is_multipart():
                # Recorrer las partes del correo
                for part in mensaje.walk():
                    # Extraer el contenido
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # el cuerpo del correo
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass

#print (body)
cadena_usuario = body.split(":")

cadena_usuario_final = cadena_usuario[1].split("<")
usuario = cadena_usuario_final[0]

cadena_pass_final = cadena_usuario[2].split("<")
pass_ = cadena_pass_final[0]

cadena_correo_final = cadena_usuario[4].split("\"")
correo = cadena_correo_final[0]

usuario = usuario.replace(" ", "")

print ("------------> %s" % (usuario))
print ("------------> %s" % (pass_))
print ("------------> %s" % (correo))

imap.close()
imap.logout()

pyad.set_defaults(ldap_server="",username="",password="")

#Añade tus credenciales del AD 

ou=pyad.adcontainer.ADContainer.from_dn("ou=,dc=,dc=")
new_user=pyad.aduser.ADUser.create("", ou, password="")

