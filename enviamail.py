import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sistemanemesis18@gmail.com', 'Nemesis2021!')
