
# -*- coding: cp1252 -*-
import sys, smptlib, re
from bottle import get, post, request, run
import re
global username, firstname, lastname, mejl, age, adress, password1, password2


"""Denna metoden ska registrera anv�ndare 
"""
@route("/registreraAnvandare/", metodh="POST")
def createUser():
   """
     username = raw_input('Ange ett anv�ndarnamn')
    firstname = raw_input('Ange ditt f�rnamn')
    lastname = raw_input('Ange ditt efternamn')
    mejl = raw_input('Ange din email')
    age = raw_input('Ange din �lder') #beh�ver vi de?
    adress = raw_input('Ange din adress')
    password1 = raw_input('Ange ett l�senord')
    password2 = raw_input('Ange l�senordet igen')
     """

    str(firstname)
    str(lastname)

    firstname.lower()
    lastname.lower()
    username.lower()
    mejl.lower()
    adress.lower()

    
<<<<<<< HEAD
    username = request.forms.username
    firstname = request.forms.firstname
    lastname = request.forms.lastname
    mejl = request.forms.mejl
    adress = request.forms.adres
    age = request.forms.age
    password1 = request.forms.password1
    password2 = request.forms.password2
        if(password1 == password2):
            print "the password match"
            return True #os�ker p� vad som ska skrivas h�r man kanske b�r g�ra
                        #en lista?
        else:
            return "L�senordet matchar ej"
            
    
=======

""" /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/.

/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b'
vet inte vilket som �r b�st �n
"""
<<<<<<< HEAD
>>>>>>> parent of b1d66e7... login 1.7
=======
>>>>>>> parent of b1d66e7... login 1.7
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

"""Metoden som ska logga in anv�ndare"""
@route("/loggain/", method = "POST")
def login():
    """userinput = raw_input('Enter your username')
    userinputPass= raw_input('Enter your password')"""
    username = request.forms.username
    password1 = request.forms.passoword1

#samma variabel namn, blir inte system f�rvirras? m�ste man d� initierar nya
    #variabelnamn?
    if username == username and password1 == password1:
        print "you're in"
    elif username != username:
        print "invalid username"
    elif password1 != password1:        print 'invalid password'
    else:
        emailFromPython()



@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)




    
