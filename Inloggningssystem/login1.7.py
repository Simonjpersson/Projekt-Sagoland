# -*- coding: cp1252 -*-
import sys, smptlib, re
from bottle import get, post, request, run
import re
global username, firstname, lastname, mejl, age, adress, password1, password2

def createUser():
    firstname = raw_input('Ange ditt f�rnamn')
    lastname = raw_input('Ange ditt efternamn')
    mejl = raw_input('Ange din email')
    age = raw_input('Ange din �lder') #beh�ver vi de?
    adress = raw_input('Ange din adress')
    password1 = raw_input('Ange ett l�senord')
    password2 = raw_input('Ange l�senordet igen')
    username = raw_input('Ange ett anv�ndarnamn')  

    str(firstname)
    str(lastname)

    firstname.lower()
    lastname.lower()
    username.lower()
    mejl.lower()
    adress.lower()

    

""" /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/.

/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
vet inte vilket som �r b�st �n
"""
    def validateEmail(mejl):
        min_len, max_domain = 1,4
       symbols = '/^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/.'  
        if re.match(symbols, mejl) 
            return True
        else
            return False
        mejl = raw_input('skriv email igen')

    

#skicka email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
def emailFromPython():
    message = MIMEMultipartI()
    message['from'] ='sagoland@gmail.com'
    message['to']= mejl
    message['subject'] = 'email'
"""tanken �r att i theMessage ska man skicka det nya l�senordet
som l�r v�l h�mtas fr�n databasen om man inte skickar nytt
"""
    theMessage = 'H�r �r ditt nya l�senord'
    message.attach(MIMEText(theMessage))
#denna funkar bara till gmail 
    mailserver = smtplib.SMTP('smtp.gmai.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('sagoland@gmail.com', 'l�senord')
    mailserver.sendmail('sagoland@gmail.com', mejl, theMessage.as_String())
    mailserver.quit()



def login():
    userinput = raw_input('Enter your username')
    userinputPass= raw_input('Enter your password')
    if userinput == mejl and userinputPass == password1:
        print "you're in"
    elif userinput != mejl:
        print "invalid username"
    elif userinputPass != password1:
        print 'invalid password'
    else:
        emailFromPython()



@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
    
