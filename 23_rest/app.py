import json
from flask import Flask, render_template, request
from urllib.request import urlopen

app = Flask(__name__)

url = "https://api.nasa.gov/planetary/apod?api_key="
myAPIfile = open("key_nasa.txt")
myAPI = myAPIfile.read()
resp = urlopen(url+myAPI)
data = json.loads(resp.read())


@app.route('/')
def display():
    return render_template("main.html", i0 = data["hdurl"], i1 = data["url"], exp = data["explanation"], dt=data["date"])


if __name__ == "__main__": #false if this file imported as module
    app.debug = True
    app.run()
