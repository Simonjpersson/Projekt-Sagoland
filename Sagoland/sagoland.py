# -*- coding: utf8 -*-x
#authors: Mimmi Castmo, Marielle Moreira Lucana, Emma Persson Wik, Simon Persson och Pernilla Stagnebo
"""from bottle import *"""
from bottle import route, run, template, request, static_file, default_app
import re, sys, mysql.connector
import getpass
import smtplib
from validate_email import validate_email


class functions():
    
        """Puts in CSS-files and pics"""
        @route('/static/<filename>')
        def serve_static(filename):
                return static_file(filename, root ="static")


        """Handels database connection """
        def handelsUsers():
                con=mysql.connector.connect(username=username, mejl=mejl, password1=password1, host="localhost", database="sagoland")
                cursor=con.cursor()







"""STARTSIDAN"""
@route('/')
def startsida():
        """Kör startsidan"""
        return template("index")







"""KONTAKTA OSS"""
@route('/contact')
def contact_us():
        """Kontakta oss sidan"""
        return template("Contact/contact1")


@route('/contact/thank-you')
def thank_you():
        """Sidan man kommer till när man har skickat ett mail till oss"""
        return template("Contact/thanks")







"""LOGGA IN"""
"""
I den här koden ska man kunna logga in, registrera och ändra användarinformation.
Koden ansluter sig till en databas som lägger in användare och som kan ändra en
användares information
"""

"""Registers users """
@route("/loggain/", method ="POST")
def regUsers():
        global username, mejl

        username = request.forms.username
        mejl=request.forms.mejl
        password1=request.forms.password1
        password2=request.forms.password2

        if password1==password2:
            if validate_email(mejl, verify=True):
            #här finns en mysql
                query('INSERT user(username, mejl, password1)' ' VALUES(%s,%s,%s)', (username, mejl, password1))
                return template("Login/loggain", title=username, username=username, mejl=mejl, password1=password1,password2=password2)
        

        else:
            "invalid credentials"


"""User logs in and is then directed to the write-page """
@route("/loggain/", method="POST")
def signIn():
        global username

        username=request.forms.username
        password1=request.forms.password1

    
        if username and password1 == cursor.execute("SELECT username, password1 FROM user WHERE %s, %s",(username, password1)):
            return template("write", title=username, username=username, password1=password1)
        else:
            cursor.close()
            "invalid credentials"


"""When user logs in they're directed towards the writing page """
@route("/write/")
def write():
        return template("Write/write")


""" you will be aple to edit a user information here"""
@route("/edituser/", method ="POST")
def editUser():
        global username,mejl, password1, password2

        username=request.forms.username
        mejl = request.forms.mejl
        password1 = request.forms.password1
        password2=request.forms.password2

        if password1==password2:
            "INSERT INTO user" "(mejl, password1)" "VALUES(%s, %s)",(mejl, password1)

            return template("/editusers/", title=username, username=username, mejl=mejl, password1=password1)
        else:
            "something went wrong, try again"



"""WRITE"""
@route('/Write/write2')
def write():
        """Kör Skriva-sidan"""
        return template("Write/write2")

@route('/Write/write3')
def write():
        """Kör Skriva-sidan"""
        return template("Write/write3")

@route('/Write/write4')
def write():
        """Kör Skriva-sidan"""
        return template("Write/write4")

@route('/Write/continue')
def write():
        """Sidan man kommer till när man vill fortsätta på en påbörjad saga"""
        return template("Write/continue")













"""READ"""
@route('/read')
def read():
        """Kör Läsa-sidan som visar alla sagor"""
        return template("Read/read")




"""KOD TILL FLICKAN MED DE MAGISKA KRITORNA"""
@route('/Read/FMDMK-names')
def story_fmdmk_names():
    """Flickan med de magiska kritorna - välja nytt namn"""
    return template("Read/FMDMK-names")

    
@route('/Read/FMDMK-front', method="POST")
def get_names():
    """Flickan med de magiska kritorna - framsidan."""
    """Sparar det nya namnet användaren valt."""
    """Skriver ut det nya namnet."""
    name = request.forms.name
    
    user_input = open("Read/text/name.txt", 'w')
    user_input.write(name)
    user_input.close()

    return template("Read/FMDMK-front", name=name)


@route('/Read/FMDMK-1')
def replace_name():
    """Flickan med de magiska kritorna - sida 1"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida1.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-1", text=text, name=name)


@route('/Read/FMDMK-2')
def replace_name():
    """Flickan med de magiska kritorna - sida 2"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida2.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-2", text=text, name=name)


@route('/Read/FMDMK-3')
def replace_name():
    """Flickan med de magiska kritorna - sida 3"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida3.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-3", text=text, name=name)


@route('/Read/FMDMK-4')
def replace_name():
    """Flickan med de magiska kritorna - sida 4"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida4.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-4", text=text, name=name)


@route('/Read/FMDMK-5')
def replace_name():
    """Flickan med de magiska kritorna - sida 5"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida5.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-5", text=text, name=name)

    
@route('/Read/FMDMK-6')
def replace_name():
    """Flickan med de magiska kritorna - sida 6"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida6.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-6", text=text, name=name)


@route('/Read/FMDMK-7')
def replace_name():
    """Flickan med de magiska kritorna - sida 7"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida7.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-7", text=text, name=name) 


@route('/Read/FMDMK-8')
def replace_name():
    """Flickan med de magiska kritorna - sida 8"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida8.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-8", text=text, name=name) 


@route('/Read/FMDMK-9')
def replace_name():
    """Flickan med de magiska kritorna - sida 9"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida9.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-9", text=text, name=name)


@route('/Read/FMDMK-10')
def replace_name():
    """Flickan med de magiska kritorna - sida 10"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida10.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-10", text=text, name=name)


@route('/Read/FMDMK-11')
def replace_name():
    """Flickan med de magiska kritorna - sida 11"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida11.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-11", text=text, name=name)


@route('/Read/FMDMK-12')
def replace_name():
    """Flickan med de magiska kritorna - sida 12"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida12.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-12", text=text, name=name)


@route('/Read/FMDMK-13')
def replace_name():
    """Flickan med de magiska kritorna - sida 13"""
    """Funktionen öppnar textfilen för sidan och söker upp name."""
    """När den hittar detta ordet ersätter den det med vad användaren matat in på namnsidan."""
    getname = open("Read/text/name.txt", 'r')
    name = getname.read()

    textfile = open("Read/text/Sida13.txt", "r")
    searchname = textfile.read()
    text = searchname.replace('name',name)
    
    getname.close()
    textfile.close()
    
    return template("Read/FMDMK-13", text=text, name=name) 




"""KOD TILL PRINSESSAN PÅ ÄRTEN"""
@route('/Read/PPA0')
def story_fmdmk_names():
    """Prinsessan på ärten framsida"""
    return template("Read/PPA0")

@route('/Read/PPA-1')
def story_fmdmk_names():
    return template("Read/PPA-1")

@route('/Read/PPA-2')
def story_fmdmk_names():
    return template("Read/PPA-2")

@route('/Read/PPA-3')
def story_fmdmk_names():
    return template("Read/PPA-3")

@route('/Read/PPA-4')
def story_fmdmk_names():
    return template("Read/PPA-4")

@route('/Read/PPA-5')
def story_fmdmk_names():
    return template("Read/PPA-5")

@route('/Read/PPA-6')
def story_fmdmk_names():
    return template("Read/PPA-6")













run(debug=True, reloader=True, host='localhost', port=8080)
