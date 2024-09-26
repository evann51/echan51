# Michelle Zhu, Jacob Lukose, Abidur Rahman, Evan Chan
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)            # create instance of class Flask

@app.route("/")                  # assign fxn to route
def hello_world():
    return "No hablo queso!"     # prints this on webpage

app.run()
