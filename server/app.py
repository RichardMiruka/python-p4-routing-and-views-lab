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
    return param  #and returns the parameter as the response to display it in the web browser.

#In this code, a new route /count/<int:param> is defined
@app.route('/count/<int:param>')                      #<int:param> is a URL parameter that represents the integer parameter for the count view.
def count(param):                                     #The function takes the param parameter, generates a range of numbers from 0 to param, and joins them together with newline characters ('\n')
    numbers = '\n'.join(str(i) for i in range(param))
    numbers += '\n'                                   # Add trailing newline character
    return numbers                                    #The resulting string with numbers on separate lines is returned as the response.

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    if operation=='+':
        result = num1 + num2
    elif operation=='-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
            result = num1 / num2
    elif operation == '%':
        result = num1 % num2  
    else:
        return 'Invalid operation'
    
    return str(result)
                 
if __name__ == '__main__':
    app.run(port=5555, debug=True)
