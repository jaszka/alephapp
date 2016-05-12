# coding=utf-8
import smtplib

def send(adres, matches):
    to = adres
    subject = 'Twoja zamówiona książka czeka na odbiór'
    text = 'Drogi Czytelniku,' \
           '\nTwoje zamówienie jest gotowe do odbioru.' \
           '\nStatus: %s.' \
           '\nWejdź na http://katalog.biblioteka.wroc.pl/F i sprawdź jeśli mi nie ufasz:P' % matches
    sender = 'mty.python@o2.pl'
    passw = 'Python123'

    mail = smtplib.SMTP('poczta.o2.pl', 587)

    mail.ehlo()
    mail.starttls()
    mail.login(sender, passw)

    body = '\r\n'.join([
        'To: %s' % to,
        'From: %s' % sender,
        'Subject: %s' % subject,
        '',
        text
    ])

    mail.sendmail(sender, [to], body)
    mail.close()
