# -*- coding: cp1252 -*-
from bottle import *
import re, sys


"""Puts in CSS-files and pics"""
@route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root ="static")

    
"""Inloggningsidan """
@route("/")
def homepage():
    
    return template("index")

"""Handels database connection """
def handelsUsers():
    con=mysql.connector.connect(username=username, mejl=mejl, password1=password1, host="localhost", database="sagoland")
    cursor=con.cursor()

"""Startsidan"""
@route("/sagoland/")
def sagoland():
    return template("sagoland")

"""Läs Saga sidan"""
@route("/read/")
def read():
    return template("read")

"""Skriv Saga Sidan"""
@route("/write/")
def login():
    return template("write")

"""Skriv Saga Sidan"""
@route("/continue/")
def continu():
    return template("continue")

"""Skriv Saga Sidan"""
@route("/write2/")
def write2():
    return template("write2")

"""Skriv Saga Sidan"""
@route("/write3/")
def write3():
    return template("write3")

"""Skriv Saga Sidan"""
@route("/write4/")
def write4():
    return template("write4")

"""Kontakta oss Sidan"""
@route("/contact1/")
def contactus():
    return template("contact1")

"""Flickan med de magiska kritorna"""
@route("/FMDMK-front/")
def FMDMKfront():
    return template("FMDMK-front")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-names/")
def FMDMKnames():
    return template("FMDMK-names")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-1/")
def FMDMK1():
    return template("FMDMK-1")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-2/")
def FMDMK2():
    return template("FMDMK-2")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-3/")
def FMDMK3():
    return template("FMDMK-3")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-4/")
def FMDMK4():
    return template("FMDMK-4")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-5/")
def FMDMK5():
    return template("FMDMK-5")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-6/")
def FMDMK6():
    return template("FMDMK-6")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-7/")
def FMDMK7():
    return template("FMDMK-7")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-8/")
def FMDMK8():
    return template("FMDMK-8")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-9/")
def FMDMK9():
    return template("FMDMK-9")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-10/")
def FMDMK10():
    return template("FMDMK-10")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-11/")
def FMDMK11():
    return template("FMDMK-11")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-12/")
def FMDMK12():
    return template("FMDMK-12")
"""Flickan med de magiska kritorna"""
@route("/FMDMK-13/")
def FMDMK13():
    return template("FMDMK-13")







run(debug=True, reloader=True, host="localhost", port=8080)        
        
        


    
                   
    
            

    
    
