import sys
#to fix: message when username/password wrong
#how to add multiple users

username = "Marielle"
password = "Lucana"
print "Username: Marielle and Password: Lucana"
print"READ TEXT BELOW"
print "When you hit enter after you entered your password and username the program will close"

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
    raw_input(enter)
    #sys.exit(0)
else:
    print"Incorrect username or password"
raw_input(enter)
#sys.exit(0)
