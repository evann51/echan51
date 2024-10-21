#Jason Chao, Victor Casado, Evan Chan
#The Flying Mice
#SoftDev
#18 - CSS Mimicry
#2024 - 10 - 16
#Time spent: 0.2 hours

from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)

@app.route('/')
def load_page():
    return render_template("mimic.html")

if __name__ == "__main__": #false if this file imported as module
    app.debug = True
    app.run()
