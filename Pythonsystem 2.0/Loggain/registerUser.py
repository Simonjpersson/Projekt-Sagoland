# -*- coding: cp1252 -*-
from bottle import get, post, request, run, static_file, template, route, response
import re, sys
#bottle.TEMPLATE_PATH.insert(0, Loggain_path)

""" Registrerar en användare """

@route('/static/<filename>')
def serve_static(filename):
    """Lägger in CSS-filen samt bilderna"""
    return static_file(filename, root ="static")

""" Hanterar användare genom att ansluta till databasen """
def handelsUsers():
    con = mysql.connector.connect(username=username, password1= password1, host='localhost', database='sagoland')

@route('/Loggain', method="POST")
def regUser():
    #global username, password1, password2, mejl
    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2

    if(password1 == password2):
        if validate_email(mejl, verify=True):
            cursor=con.cursor()
            query=("INSERT user(username, mejl, password1, password2)""VALUES(%s,%s,%s)",(username, mejl, password1, password2))
            cursor.execute(query)
    else:
            "<p>Ett fel har inträffat<p>"
            
    return template("loggain", username=usernames)

run(host="localhost", port=8080, debug=True, reloader=True)
    
