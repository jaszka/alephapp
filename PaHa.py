# coding=utf-8
import functions

'''
Paha to Twoja podręczna ciocia bibliotekarka, która zawsze wie, kiedy masz iść odebrać swoją zamówioną książkę.
Słuchaj się cioci. A najpierw podaj swój login i hasło do katalogu Aleph, i maila na którego ciocia ma wysyłać całuski
'''

data = functions.read()

(reservationReady, notification) = functions.checkAleph(data['id'], data['key'])

if (reservationReady):
    functions.send(notification, data['to'])
