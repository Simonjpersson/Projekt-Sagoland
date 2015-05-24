from bottle import route, run, template, request, static_file
#import mysql.connector
# Author: Marielle 
"""from validate_email import validate_email"""
"""Den klassen testar att ansluta sig till index-sidan """

"""Puts in CSS-files and pics"""
class testing():
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
