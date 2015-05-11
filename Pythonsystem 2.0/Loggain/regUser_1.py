# -*- coding: cp1252 -*-
from bottle import get, post, request, run, static_file, template, route
import re, sys

from bottle import response

@route('/static/<filename>')
def serve_static(filename):
    """Lägger in CSS-filen samt bilderna"""
    return static_file(filename, root ="static")

@route('/')
def runpage():
    return template("loggain")
    




'''Har inte så stor koll på nedan del, Marielle så gör allt grönt
sålänge så får du "akivera" varje funktion som funkar. Just nu när
man kör så kommer den i vart fall till inloggningssidan :)




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
Vart ska användaren ta vägen när användaren är inne?
Det kan skrivas in här iaf"""
@route("/", method = "POST")    
def usersHomepage():
    global username

    return template("/", username = username) '''

run(debug = True, reloader = True, host = 'localhost', port = 8080)


