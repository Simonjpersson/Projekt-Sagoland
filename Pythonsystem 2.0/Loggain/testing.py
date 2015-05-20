from bottle import route, run, template, request, static_file
#import mysql.connector
# Author: Marielle 
"""from validate_email import validate_email"""

"""Puts in CSS-files and pics"""
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


@route("/contact1/")
def contactus():

    return template("contact1")

run(reloader=True, debug=True, host="localhost", port =8080)
