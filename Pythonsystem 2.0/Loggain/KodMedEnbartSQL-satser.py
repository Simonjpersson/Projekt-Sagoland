# -*- coding: cp1252 -*-
""" I den här filen finns alla SQL-satser som använts. Detta är enbart för
    att visa vilka sql-sater som använts till respektive metod """

# -*- coding: cp1252 -*-
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
""" SQL-satsen för att insert user och på username sätts
    DUPLICATE KEY UPDATE för att göra det unikt """
@route("/", method = 'POST')
def runpage():
        if validate_email(mejl, verify = True):            
            con = mysql.connector.connect(host='localhost', database ='sagoland')
            cursor = con.cursor()
            query = ("INSERT user(username, mejl, password1)" "VALUES(%s,%s,%s)", (username, mejl, password1))ON DUPLICATE KEY UPDATE username = username;    
            cursor.execute(query)
    else:
        "Ett fel har inträffat, det kan bero på att användarnamnet redan existerar"+
        " eller pga du har angivit fel information"

    return template("loggain")


"""Användare loggar in"""
"""SQL-sats har satts in för att hämta in användarnamn osv """
@route("/")
def signinUser(username, password1):
     con = mysql.connector.connect(username=username, password1=password1, host='localhost', database='sagoland') 
        cursor.execute("SELECT username, password1 FROM user")
    
        if username and password1 == "SELECT username, password1 FROM user":
            return True
        return template("/", username = username)
            else:
            cursor.close()
            return "<p> Inloggning misslyckats. Försök igen! <p>"



""" Användarens sida kommer att dirigera om till dens sida
    dvs skriva-sidan """
@route("/")
def userLoggedIn():
    return template("/", username=username)




""" ändra användares info"""
""" SQL hämtar username och password1 från user """
""" Med insert into user sätts nya värden in """
@route ("/")    
def editUser():
    con = mysql.connector.connect(username=username, password1=password1, host='localhost', database='sagoland')
    if username and password1 == "SELECT username, password1 FROM user":
        "INSER INTO user""(username, mejl, password1)" "VALUES(%s, %s, %s,)"(username, mejl, password1))ON DUPLICATE KEY UPDATE username = username   
       
     return template("/", username=username, mejl=mejl, password1=password1, password2=password2)



        
runt(debug=True, reloader=True, host='localhost', port=8080)
