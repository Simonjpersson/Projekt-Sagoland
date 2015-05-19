# -*- coding: cp1252 -*-
from bottle import get, post, request, run, static_file, template, route, response
import re, sys

from bottle import route, run

@route('/static/<filename>')
def serve_static(filename):
    """L�gger in CSS-filen samt bilderna"""
    return static_file(filename, root ="static")

def handelsUsers():
    con = mysql.connector.connect(username=username, password1=password1, host='localhost', database='sagoland') 

"""Helhetsagoland i mappen write, sidan write"""
""" f�rsta sidan """
@route("/write")
def homePage():
    return template("write")

"""Loggain fil i loggain mappen.
    Emil s�ger att jag borde kopierat.
    R�tt filer i r�tt mappar
    Route-kopplar inte till fil utan till mappen"""


@route("/Loggain", method ="GET")
def registerUser():
    
   return template("loggain")

"""Tar emot inneh�llet fr�n formul�ret och updaterar sidan """
@route("/update/", method ="POST")
def updateRegisterUser():
    global username, mejl, password1, password2
    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2

    """ username �r satt som unik i databasen"""
    if(password1 == password2):
        """ validerar email med hj�lp av validate_email fr�n pip """
        if validate_email(mejl, verify = True):
            #h�r fanns en mysql connection innan den finns nu i metoden handelsUsers
            cursor = con.cursor()
            query = ("INSERT user(username, mejl, password1)" "VALUES(%s,%s,%s)", (username, mejl, password1));
            cursor.execute(query)
    else:
        "Ett fel har intr�ffat, det kan bero p� att anv�ndarnamnet redan existerar eller pga du har angivit fel information"

    
    return template("update", username= username)

"""loggin-sida, ligger i helhetsagoand"""
@route("/Loggain/", method = "POST")
def signinUser(username, password1):
    global username, mejl, password1, password2
    username = request.forms.username
    password1= request.forms.passwords1
    username = request.forms.username
    password1 = request.forms.password1
    cursor.execute("SELECT username, password1 FROM user WHERE %s", (username) )
    
    if username and password1 == "SELECT username, password1 FROM user":     
        return template("/", username = username)
        else:
            cursor.close()
    return "<p> Inloggning misslyckats. F�rs�k igen! <p>"


""" Anv�ndarens sida kommer att dirigera om till dens sida
    dvs skriva-sidan """
@route("/")
def userLoggedIn():
    return template("/", username=username)


""" �ndra anv�ndares kan redigera sin information"""
@route ("/")    
def editUser():
    global username, mejl, password1, password2
    con = mysql.connector.connect(username=username, password1=password1, host='localhost', database='sagoland')
    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2
    if username and password1 == "SELECT username, password1 FROM user":
        "INSER INTO user""(username, mejl, password1)" "VALUES(%s, %s, %s,)"(username, mejl, password1))ON DUPLICATE KEY UPDATE username = username   
       
     return template("/", username=username, mejl=mejl, password1=password1, password2=password2)



run(debug=True, host='localhost', port=8080, reloader = True)

