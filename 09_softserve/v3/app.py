# Evan Chan
# SoftDev
# September 2024

from flask import Flask               #imports Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():                    #defines new function
    print("about to print __name__...") #prints in terminal
    print(__name__)                     #prints in terminal
    return "No hablo queso!"          #prints "No hablo queso!" on the webpage

app.debug = True        #sets debug to true
app.run()       #runs app
