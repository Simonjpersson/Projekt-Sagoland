

def list():
    
    userslist = []

    username = request.forms.username
    mejl=request.forms.mejl
    password1=request.forms.password1
    password2=request.forms.password2

    if password1==password2:
        userlist.extend(username, mejl, password1 "/static/user/")
        mail = mejl+".txt"
        if mail in userlist("username"):
            return "exist"

        else:
            save_user=open("username/" + email +".txt")

             for i in userlist:
                 saver_user.write(i)
                 saver_user.write("\n")

                 save_user.closer()

                 f=open("user/" + email +".txt")
                 saver_user=f.readlines()
                 f.close()
                 return template("loggain", title=username, mejl=mejl, password1=password1)
    else:
        return"something went wront"

            
                 
        
