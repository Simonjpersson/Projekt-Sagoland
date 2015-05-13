# -*- coding: cp1252 -*-
"""Koden är utan SQL-satser och hämtar bara in info som skrivs in """

from bottle import get, post, request, run, static_file, template, route, response
import re, sys, mysql.connector
import getpass
import smtplib
from validate_email import validate_email


@route('/static/<filename>')
def serve_static(filename):
    """Lägger in CSS-filen samt bilderna"""
    return static_file(filename, root ="static")



""" Registerar användare """
@route("/loggain/", method = 'POST')
def runpage():
    global username, mejl, password1, password2
    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2

""" username är satt som unik i databasen"""
    if(password1 == password2):
        """ validerar email med hjälp av validate_email från pip """
        if validate_email(mejl, verify = True):            
            
    else:
        "Ett fel har inträffat, det kan bero på att användarnamnet redan existerar"+
        " eller pga du har angivit fel information"

    return template("loggain")


"""Användare loggar in"""
@route("/")
def signinUser(username, password1):
    global username, mejl, password1, password2
        if username and password2:
            return True
        return template("/", username = username)
            else:
            return False
        return "<p> Inloggning misslyckats. Försök igen! <p>"



""" Användarens sida kommer att dirigera om till dens sida
    dvs skriva-sidan """
@route("/")
def userLoggedIn():
    return template("/", username=username)




""" ändra användares info"""
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

