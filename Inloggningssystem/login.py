# -*- coding: cp1252 -*-


import sys, smptlib
#to fix: message when username/password wrong
#how to add multiple users

username = ""
password = ""
""" not finished
"""

""" Method for making login accounts, not finished. 
"""
def createAccount():
    if username == raw_input
    username
    while not username:
        username = input("enter login name")
        
    if password == raw_input
    password
    while not password
        password ("enter your password")
    


""" Method for the user to login, not tested with users
"""
def validation():
    print "Enter your username and password"
    user = raw_input("Enter your username: ")
    if user == username:
        print" "

    else: 
            print "Invalid username"
            raw_input(enter)
            #sys.exit(0)
            password = raw_input("Enter your password: ")

    if password == password:
        print"Correct! You're in"
        raw_inputput(enter)
        #sys.exit(0)
    else:
        print"Incorrect username or password"
    raw_input(enter)
    #sys.exit(0)



""" smtplib is a client session object, it's used to send mail to any internet
machine
This method is going to send a message, only to gmail accounts so far
"""

def emailBoot():
    content = "Fel användernamn eller lösenord"
    mail = smtplib.SMYP('smtp.gamil.com', 587)
    mail.ehlo()
    mail.startIs()
    mail.login('email', 'paassword')
    #use the same email as above
    mail.sendmail('fromEmail', 'receive', content)
    mail.close()
    




                  
    
