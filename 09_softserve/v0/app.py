# Michelle Zhu, Jacob Lukose, Abidur Rahman, Evan Chan
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # how was "__name__" defined? 

@app.route("/")                # "/" refers to root URL
def hello_world():
    print(__name__)            # prints "__main__" in terminal
    return "No hablo queso!"   # prints on web page

app.run()                      # running a method of another class?
