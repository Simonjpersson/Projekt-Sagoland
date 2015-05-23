# -*- coding: cp1252 -*-
from bottle import *
import re, sys


"""Puts in CSS-files and pics"""
@route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root ="static")

    
"""Inloggningsidan """
@route("/")
def homepage():
    
    return template("index")

"""Handels database connection """
def handelsUsers():
    con=mysql.connector.connect(username=username, mejl=mejl, password1=password1, host="localhost", database="sagoland")
    cursor=con.cursor()

"""Startsidan"""
@route("/sagoland/")
def sagoland():
    return template("sagoland")

"""Läs Saga sidan"""
@route("/read/")
def read():
    return template("read")

"""Skriv Saga Sidan"""
@route("/write/")
def login():
    return template("write")

"""Skriv Saga Sidan"""
@route("/continue/")
def continu():
    return template("continue")

"""Skriv Saga Sidan"""
@route("/write2/")
def write2():
    return template("write2")

"""Skriv Saga Sidan"""
@route("/write3/")
def write3():
    return template("write3")

"""Skriv Saga Sidan"""
@route("/write4/")
def write4():
    return template("write4")




"""Kontakta oss Sidan"""
@route("/contact1/")
def contactus():
    return template("contact1")
	
	
@route("/contact1/")
def contactus():
    return template("contact1")




run(debug=True, reloader=True, host="localhost", port=8080)        
        
        


    
                   
    
            

    
    
