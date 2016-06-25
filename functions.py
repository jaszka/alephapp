# coding=utf-8
import argparse
import urllib
import urllib2
import cookielib
import smtplib
import re
import yaml

def read():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='Login do katalogu Aleph', type=str)
    parser.add_argument('key', help='Hasło do katalogu Aleph', type=int)
    parser.add_argument('email', help='Adres email, na który ma być wysłana wiadomość', type=str)
    args = parser.parse_args()
    return {'id' : args.id, 'key' : args.key, 'to' : args.email}

def loginAleph(logon, haslo):
    url = 'http://katalog.biblioteka.wroc.pl/F'
    values = {
        'func': 'bor-hold',
        'adm_library': 'MBP50',
        'bor_id': logon,
        'bor_verification': haslo,
        'bor_library': 'MBP50'
    }
    data = urllib.urlencode(values)

    cookies = cookielib.CookieJar()
    opener = urllib2.build_opener(
        urllib2.HTTPRedirectHandler(),
        urllib2.HTTPHandler(debuglevel=0),
        urllib2.HTTPSHandler(debuglevel=0),
        urllib2.HTTPCookieProcessor(cookies))

    response = opener.open(url, data)
    page = response.read()
    return page

def checkAleph(logon, haslo):
    page = loginAleph(logon, haslo)
    notification = re.findall('Zarezerwowany.+\d', page)
    #notification = 'bla'
    if len(notification)>0:
        return (True, notification)
    else:
        return (False, notification)

def load_file(filepath):
    with open(filepath, 'r') as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def send(notification, to):
    data = load_file('config.yml')
    smtp = data.get('smtp')
    mail = smtplib.SMTP(smtp['host'], smtp['port'])
    mail.ehlo()
    mail.starttls()
    mail.login(smtp['sender'], smtp['password'])

    subject = 'Twoja zamówiona książka czeka na odbiór'
    text = 'Drogi Czytelniku,' \
        '\nTwoje zamówienie jest gotowe do odbioru.' \
        '\nStatus: %s.' \
        '\nWejdź na http://katalog.biblioteka.wroc.pl/F i sprawdź jeśli mi nie ufasz:P' % notification

    body = '\r\n'.join([
        'To: %s' % to,
        'From: %s' % smtp['sender'],
        'Subject: %s' % subject,
        '',
        text
        ])

    mail.sendmail(smtp['sender'], [to], body)
    mail.close()
    print 'Poszło'

if __name__ == '__main__':
    test = checkAleph('200706', '813344')
    print test

#logon = '200706'
#haslo = '813344'
#adres = 'a.jachowicz@o2.pl'