# -*- coding: cp1252 -*-
from bottle import Bottle, get, post, request, run, static_file, template, route, response, TEMPLATE_PATH
"""from validate_email import validate_email"""
import smtplib, re, sys, mysql.connector


@route('/static/<filename>')
def serve_static(filename):
    """Lägger CSS-filen + bilderna """
    return static_file(filename, root="static")
    
def handelsUsers():
    con = mysql.connector.connect(username=username, password1=password1, host='localhost', databse='sagoland')

    #con = mysql.connector.connect(username='[username]', password1='[password1]',mejl='[mejl]', host='localhost', databse='sagoland')
    cursor = con.cursor()
    cursor.execute() 



    
@route('/')
def registerUser():
    global username, mejl, password1, password2
    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2

    if (password1 == password2):
        if validate_email(mejl, verify = True):
            return "awesome"

    else:
        "fel"
    return template("loggain")

    
run(debug=True, host = "localhost", port = 8080, reloader=True)
