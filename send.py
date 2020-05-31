import smtplib
from email.mime.text import MIMEText


smtp_ssl_host = 'smtp.example.com'
smtp_ssl_port = 465

username = 'example@mail.com'
password = 'password'

from_addr = 'example@mail.com'
to_addrs = ['example@mail.com']



message = MIMEText('Hello World')
message['subject'] = 'Hello'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)


server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()
