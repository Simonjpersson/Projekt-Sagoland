from bottle import request, run, route, request, template
import sys

@route ('/')
def user():
    return template("inlogg")

run(debug = True, reloader = True, host = 'localhost', port = 8080)
