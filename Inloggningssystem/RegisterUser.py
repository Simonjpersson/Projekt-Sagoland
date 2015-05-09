# -*- coding: cp1252 -*-
import sys, smptlib, re
from bottle import get, post, request, run, route, request, static_file, template
import re



"""Denna metoden ska registrera användare 
"""
@route('/')
def createUser():
 """  global username, firstname, password1, password2
    username.lower()
    mejl.lower()
    adress.lower()

    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2
        if(password1 == password2):
            print "the password match"
            return True 
        else:
            return "Lösenordet matchar ej" """
        return template("inlogg")
        

    

    """        
    def validateEmail(mejl):
        min_len, max_domain = 1,4
        symbols = '/^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/.'  
        if re.match(symbols, mejl) 
            return True
        else
            return False
        mejl = raw_input('skriv email igen') """

run(debug True, reloader = True, host = 'localhost', port = 8080)
