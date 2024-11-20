import json, urllib
from flask import Flask, render_template, request

app = Flask(__name__)

url = "https://api.nasa.gov/planetary/apod?api_key="
myAPIfile = open("key_nasa.txt")
myAPI = myAPIfile.read()
img = ""

@app.route('/')
def display():
    

    return render_template("main.html", apiKey = myAPI)


if __name__ == "__main__": #false if this file imported as module
    app.debug = True
    app.run()
