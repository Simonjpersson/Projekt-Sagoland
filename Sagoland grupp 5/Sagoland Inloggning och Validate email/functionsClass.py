# -*- coding: cp1252 -*-
from bottle import route, run, template, request, static_file
import re, sys, mysql.connector
import getpass
import smtplib
from validate_email import validate_email


"""I den här koden ska man kunna logga in, registrera och ändra användarinformation"""
""" Koden ansluter sig till en databas som lägger in användare och som kan ändra en användares information """
""" Koden använder sig pip och validate_email som måste installeras innan koden kan köras"""

class functions():
    

    @route('/static/<filename>')
    def serve_static(filename):
        return static_file(filename, root ="static")


"""Handels database connection """
    def handelsUsers():
        con=mysql.connector.connect(username=username, mejl=mejl, password1=password1, host="localhost", database="sagoland")
        cursor=con.cursor()


    
"""Homepage """
    @route("/")
    def homepage():
    
        return template("index")



"""Registers users """
    @route("/loggain/", method ="POST")
    def regUsers():
        global username, mejl

        username = request.forms.username
        mejl=request.forms.mejl
        password1=request.forms.password1
        password2=request.forms.password2

        if password1==password2:
            if is_valis= validate_email(mejl, check_mx=True):
            #här finns en mysql
                query('INSERT user(username, mejl, password1)' ' VALUES(%s,%s,%s)', (username, mejl, password1))
                return template("loggain", title=username, username=username, mejl=mejl, password1=password1,password2=password2)
        

        else:
            "invalid credentials"


"""User logs in and is then directed to the write-page """
    @route("/loggain/", method="POST")
    def signIn():
        global username

        username=request.forms.username
        password1=request.forms.password1

    
        if username and password1 == cursor.execute("SELECT username, password1 FROM user WHERE %s, %s",(username, password1)):
            return template("write", title=username, username=username, password1=password1)
        else:
            cursor.close()
            "invalid credentials"


"""When user logs in they're directed towards the writing page """
    @route("/write/")
    def write():
        return template("write")


""" you will be aple to edit a user information here"""
    @route("/edituser/", method ="POST")
    def editUser():
        global username,mejl, password1, password2

        username=request.forms.username
        mejl = request.forms.mejl
        password1 = request.forms.password1
        password2=request.forms.password2

        if password1==password2:
            "INSERT INTO user" "(mejl, password1)" "VALUES(%s, %s)",(mejl, password1)

            return template("/editusers/", title=username, username=username, mejl=mejl, password1=password1)
        else:
            "something went wrong, try again"


    run(debug=True, reloader=True, host="localhost", port=8080)        
            

    
    
