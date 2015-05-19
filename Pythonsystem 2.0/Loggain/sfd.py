# -*- coding: cp1252 -*-
from bottle import get, post, request, run, static_file, template, route, response
import re, sys

from bottle import route, run

@route('/static/<filename>')
def serve_static(filename):
    """Lägger in CSS-filen samt bilderna"""
    return static_file(filename, root ="static")


@route("/", method ="GET")
def registerUser():
   """ global username, mejl, password1, password2
    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2

    if (password1 == password2):
        "<p> rätt lösen <p>"
    else:
        "<p> fel <p>"
            """
   return template("loggain")

run(debug=True, host='localhost', port=8080, reloader = True)

