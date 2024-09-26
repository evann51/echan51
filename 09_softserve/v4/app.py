# Michelle Zhu, Jacob Lukose, Abidur Rahman, Evan Chan
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)           # create instance of class Flask

@app.route("/")                 # assign fxn to route
def hello_world():
    print("the __name__ of this module is... ") # prints this right above "__main__"
    print(__name__)      # prints "__main__"
    return "No hablo queso!"

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
