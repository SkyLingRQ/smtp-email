#importamos las librerias necesarias
import smtplib
import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders

#configuramos el servicio smtp
    
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'gmail'
smtp_password = 'codigo de aplicacion'

#configuramos el envio a nuestro antojo

sender = 'email'
receiver = ['email que recibira el mensaje']
subject = 'asunto'
body = 'texto'

#en esta parte debebos cambiar el "imagen.png" por el archivo que quieres que se envie

filename = 'imagen.png'
attachment = open(filename, 'rb')

#creando el email a enviar

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = COMMASPACE.join(receiver)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

#envio del mensaje

part = MIMEBase('application', "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=filename)
msg.attach(part)

server = smtplib.SMTP(smtp_server, smtp_port)
server.ehlo()
server.starttls()
server.login(smtp_username, smtp_password)
server.sendmail(sender, receiver, msg.as_string())
server.close()