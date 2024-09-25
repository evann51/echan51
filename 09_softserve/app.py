# Evan Chan
# SoftDev
# September 2024

from flask import Flask               #imports Flask
import random as r

app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():                    #defines new function
    f = open("occupations.csv", "r")
    string = f.read()

    list = string.split("\n")
    list = list[1:len(list)-2] #removes example row, total row, and new line row
    dict = {}

    counter = 1

    for i in range(len(list)):
        if(list[i][0] == "\""):
            indexcomma = list[i][1:].index("\"") + 2
            name = list[i][1:indexcomma - 1] #starts at first quote, ends at second quote
            num = list[i][indexcomma + 1:]
        else:
            split = list[i].split(",")
            name = split[0]
            num = split[1]
        for k in range(int(float(num) * 10)):
            dict.update({counter: name})
            counter += 1
    return("maje_stic \n"+dict[r.randint(1, 998)])

app.debug = True        #sets debug to true
app.run()       #runs app
