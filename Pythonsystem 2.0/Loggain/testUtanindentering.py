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
def defPage():
    return template("loggain")

runt(debug=True, reloader=True, host='localhost', port=8080)
