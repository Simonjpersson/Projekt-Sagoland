# -*- coding: utf8 -*-x
#author: Pernilla Stagnebo
from bottle import route, run, template, request, static_file, default_app
from os import listdir



@route('/static/<filename>')
def serve_static(filename):
    """Lägger in CSS-filen samt bilderna"""
    return static_file(filename, root ="static")





    
@route('/FMDMK-front')
def story_fmdmk_front():
    """Flickan med de magiska kritorna - framsidan"""
    return template("FMDMK-front")


@route('/FMDMK-names')
def story_fmdmk_names():
    """Flickan med de magiska kritorna - välja nytt namn"""
    return template("FMDMK-names")


@route('/FMDMK-1')
def story_fmdmk_1():
    """Flickan med de magiska kritorna - sida 1"""
    textfile = open("text/Sida1.txt", "r")
    
    
     
    
    m = textfile.read()
    text = m.replace('name1','Julia') '''and('name2','Buster')'''
    
    
    '''replacements = {'name1':'Pernilla', 'name2':'Krysmynta'}
    for name1 in textfile:
        for src, target in replacements.iteritems():
            name1 = name1.replace(src, target)'''
    
    textfile.close()
    
    
    
    
    return template("FMDMK-1", text=text)

    





        

'''@route('/article')
def article():
    """Sidan där man skriver artiklarna"""
    return template("article")




@route("/update", method = "POST")
def form():
    """Sidan man kommer till när man har lagt till en artikel"""
    headline = request.forms.headline
    message = request.forms.message

    print headline + '.txt'

    user_input = open("wiki/" + headline + '.txt', 'w')
    user_input.write(message)
    user_input.close()

    return template ("update", headline=headline, message=message)




@route('/')
def list_articles():
    """Läser från textfilen och skriver ut rubrikerna i en lista på startsidan"""
    files = listdir("wiki")
    articles_list = []

    for row in files:
        delete_dot = row.split(".")
        word = delete_dot[0]
        delete_slash = word.split("/")
        articles_list.append(delete_slash[0])
 
    return template ('index', articles_list=articles_list)




@route('/show/<headline>')
def show_article(headline):

    """Visar användarens text för användaren"""
    
    wikifile = open("wiki/" + headline + '.txt', "r")
    message = wikifile.read()
    wikifile.close()
    return template("showarticle", headline = headline, message = message)




@route('/show/<headline>/editarticle')
def edit_article(headline):

    """Här redigerar användaren sin text"""

    wikifile = open("wiki/" + headline + '.txt', "r")
    message = wikifile.read()
    wikifile.close()

    return template ("editarticle", headline=headline, message=message)'''
  
    















run(debug=True, reloader=True, host='localhost', port=8080)
