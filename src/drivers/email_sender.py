import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "pzrbvnhqs3lapo4i@ethereal.email"
    login = "pzrbvnhqs3lapo4i@ethereal.email"
    password = "gMTENTA3wkHHDM2fsH"
    
    msg = MIMEMultipart()
    msg["from"] = "viagens_confirmar@email.com"
    msg["to"] = ', '.join(to_addrs)
    
    msg["Subject"] = "Confirmação de Viagem!"
    
    #O "plain" ali é algo básico
    msg.attach(MIMEText(body, 'plain'))
    
    #587 é uma porta padrão para o SMTP
    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()
    
    for email in to_addrs:
        server.sendmail(from_addr, email, text)
        
    server.quit()