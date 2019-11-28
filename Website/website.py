from flask import Flask, render_template, request, redirect, Response
import json, sys
sys.path.append('..')
from Python4Physics import el, eHyd, eHydDiff, freqOld
#from Elements import *

app = Flask(__name__)

def find_function(function, input1, input2):
    if function == "el":
        return el(input1)
    elif function == "eHyd":
        return eHyd(input1)
    elif function == "eHydDiff":
        return eHydDiff(input1, input2)
    elif function == "freqOld":
        return freqOld(input1, input2)

@app.route("/")
def output():
    return render_template("website.html")

@app.route('/input', methods=['POST'])
def return_answer():
    data = request.get_json()
    result = find_function(data[0], data[1], data[2])
    return str(result)

if __name__ == '__main__':
    app.run()


