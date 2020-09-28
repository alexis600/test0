import smtplib

from email.mime.text import MIMEText
#para el texto
msg = MIMEText("Contenido de mail")
msg['subject'] = 'Asunto del correo'
msg['From'] = 'alexis.600@gmail.com'
msg['To'] = 'alexis.600@gmail.com'

mailServer = smtplib.SMTP('smtp.gmail.com', 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('alexis.600@gmail.com','password')
mailServer.sendmail('alexis.600@gmail.com', 'alexis.600@gmail.com', msg_as_string())

mailServer.close()
