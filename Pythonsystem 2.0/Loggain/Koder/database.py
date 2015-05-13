# -*- coding: cp1252 -*-
"""Fredrik kod från handledningen visar hur man ansluter """"

import mysql.connector
from bottle import request, post, route, run, template

@route('/user/<username>')
def getUser(username):
    #uppkoppling
        con = mysql.connector.connect(user="sagoland", password="saga", host ="localhost", database="sagoland")
        cursor = con.cursor()

        query = "SELECT mejl, password1 FROM login WHERE mejl='" + username + "'"

        cursor.execute(query)

        for user in cursor:
            return user

run(host='localhost', port =8080)
