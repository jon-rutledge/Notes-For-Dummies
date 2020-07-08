import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)

#start Connection
conn.ehlo()
print(type(conn))
conn.starttls()


conn.login('TastyBotling@gmail.com', 'GmailBot9027!')
