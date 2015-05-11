import logging, os, re, smtplib

match = re.compiler(r'^.*\s+mail exchanger = (?P<priority>\d+) (?P<host>\S+)\s*$)
                    
def verifyEmail(adress, localAdress= 'Jane.Doe@example.com'):
                    logging.debug('Verifierar email %' adress)

           """Letar efter mail utbyte"""
                    host = adress.rsplit('@', 2)[1]
                    p =os.popen('nslookup -q = mx%s'% host,r)
