# coding=utf-8
import re
import login
import sendemail

'''
Paha to Twoja podręczna ciocia bibliotekarka, która zawsze wie, kiedy masz iść odebrać swoją zamówioną książkę.
Słuchaj się cioci. A najpierw podaj swój login i hasło do katalogu Aleph, i maila na którego ciocia ma wysyłać całuski
'''

logon = ''
haslo = ''
adres = ''

# Czy zamówienie jest juz dostępne?
matches = re.findall('Zarezerwowany.+\d', login.loginaleph(logon, haslo))

if len(matches) > 0:
    sendemail.send(adres, matches)
