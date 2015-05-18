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
@route("/", method = 'POST')
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
            con = mysql.connector.connect(host='localhost', database ='sagoland')
            cursor = con.cursor()
            query = ("INSERT user(username, mejl, password1)" "VALUES(%s,%s,%s)", (username, mejl, password1))ON DUPLICATE KEY UPDATE username = username;    
            cursor.execute(query)
    else:
        "Ett fel har inträffat, det kan bero på att användarnamnet redan existerar"+
        " eller pga du har angivit fel information"

    return template("loggain")
