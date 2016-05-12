import urllib
import urllib2
import cookielib

def loginaleph(logon, haslo):
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
