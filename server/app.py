#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')   # defined a route for the root URL in my Flask application
def index():      #view returns a simple string of HTML
    return '<h1>Python Operations with Flask Routing and Views</h1>'

#In this code, a new route '/print/<string:param>' is defined
@app.route('/print/<string:param>') # <string:param> is a URL parameter that represents the string to be printed
def print_string(param):           #The print_string function takes the param parameter, prints it in the console using print(param),
    print(param)
    return param                   #and returns the parameter as the response to display it in the web browser.

if __name__ == '__main__':
    app.run(port=5555, debug=True)
