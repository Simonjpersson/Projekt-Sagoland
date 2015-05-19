# -*- coding: cp1252 -*-
from bottle import get, post, request, run, static_file, template, route, response
import re, sys

from bottle import route, run

@route('/static/<filename>')
def serve_static(filename):
    """Lägger in CSS-filen samt bilderna"""
    return static_file(filename, root ="static")

"""Loggar in användaren"""

@route("/Loggain", method="GET")
def regUsers():

    return template("loggain")




run(host="localhost", port =8080, reloader=True, debug=True)


