# -*- coding: cp1252 -*-
from bottle import get, post, request, run, static_file, template, route, response, TEMPLATE_PATH
import re, sys

@route('/static/<filename>')
def serve_static(filename):
    """Lägger CSS-filen + bilderna """
    return static_file(filename, root="static")

@route('/')
def registerUser():
    global username, mejl, password1, password2
    username = request.forms.username
    mejl = request.forms.mejl
    password1 = request.forms.password1
    password2 = request.forms.password2

run(debug=True, host = "localhost", port = 8080, reloader=True)
