#Leon Huang, Evan CHan, Ethan Sie
#The Grizzly Bears
#SoftDev
#K13 - Combine
#2024-9-30
#Time Spent: TBD

from flask import Flask, render_template
import random as r

app = Flask(__name__)

def makeStr():
    f = open("data/occupations.csv", "r")
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
    print(dict)
    return dict

@app.route("/wdywtbwygp")
def showT():
    return render_template( 'tablified.html', teamname="The Grizzly Bears",collection = makeStr().values())




if __name__ == "__main__":
    app.debug = True
    app.run()
