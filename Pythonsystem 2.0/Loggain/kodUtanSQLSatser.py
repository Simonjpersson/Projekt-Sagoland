# -*- coding: cp1252 -*-
"""Koden �r utan SQL-satser och h�mtar bara in info som skrivs in """

from bottle import get, post, request, run, static_file, template, route, response
import re, sys, mysql.connector
import getpass
import smtplib
from validate_email import validate_email


@route('/static/<filename>')
def serve_static(filename):
    """L�gger in CSS-filen samt bilderna"""
    return static_file(filename, root ="static")



""" Registerar anv�ndare """
@route("/loggain/", method = 'POST')
def runpage():
    global username, mejl, password1, password2
    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2

""" username �r satt som unik i databasen"""
    if(password1 == password2):
        """ validerar email med hj�lp av validate_email fr�n pip """
        if validate_email(mejl, verify = True):            
            
    else:
        "Ett fel har intr�ffat, det kan bero p� att anv�ndarnamnet redan existerar"+
        " eller pga du har angivit fel information"

    return template("loggain")


"""Anv�ndare loggar in"""
@route("/")
def signinUser(username, password1):
    global username, mejl, password1, password2
        if username and password2:
            return True
        return template("/", username = username)
            else:
            return False
        return "<p> Inloggning misslyckats. F�rs�k igen! <p>"



""" Anv�ndarens sida kommer att dirigera om till dens sida
    dvs skriva-sidan """
@route("/")
def userLoggedIn():
    return template("/", username=username)




""" �ndra anv�ndares info"""
@route ("/")    
def editUser():
    global username, mejl, password1, password2
    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2
    if username and password1:      
       return True
     return template("/", username=username, mejl=mejl, password1=password1, password2=password2)



        
runt(debug=True, reloader=True, host='localhost', port=8080)

