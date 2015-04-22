# -*- coding: cp1252 -*-


import sys, smptlib, re
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
def validationOfUser():
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

    
#validate email
def validateEmail(email):
    if len (email) > 7:
        print "email check#
        if re.match("^¨.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email)!= None:
            return False
        return True
    else:
        return True

        



                  
    
