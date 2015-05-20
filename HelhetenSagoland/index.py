# coding: utf-8
# Author: Marielle 
from bottle import route, run, template, request, static_file
from os import listdir
import sys


@route('/static/<filname>')
def server_static(filname):
    return static_file(filname, root="HelhetenSagoland")

"""Startsidan
@route("/")
def index():
    return template("index")
    n"""

run(host="localhost", port=8080, reloader=True, debug=True)
