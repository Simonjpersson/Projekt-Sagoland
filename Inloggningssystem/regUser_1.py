# -*- coding: cp1252 -*-
from bottle import get, post, request, run, static_file, template, route
import re, sys

"""This method will register new users"""
@route("/inlogg/", method ="POST")
def createUser():
    global username, mejl, password1, password2    
    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2
    username.lower()
    mejl.lower()
    
    """if password1 == password2:
        print "password matches"
        return True"""
    return template("inlogg", username = username, mejl = mejl, password1 = password1)


"""Signing in user"""
@route ("/", method = "POST")
def login():
    global username, mejl

    username = request.forms.username
    password1 = request.forms.password1
    
    if password1 == password2:
        print "valid credentials"
        return template("inlogg", username = username, mejl = mejl)
    else:
        return "Credentials invalid"


""" Users home page,
Vart ska anv�ndaren ta v�gen n�r anv�ndaren �r inne?
Det kan skrivas in h�r iaf"""
route("/", method = "POST")    
def usersHomepage()
    global username

    return template("/", username = username)

run(debug = True, reloader = True, host = 'localhost', port = 8080)


