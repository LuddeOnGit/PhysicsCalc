from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

def find_function(function, input1, input2):
    if function == "el":
        return el(input1)

def el(λ): return (h*c)/λ

@app.route("/")
def output():
    return render_template("website.html")

@app.route('/input', methods=['POST'])
def return_answer():
    data = request.get_json()
    result = find_function(data[0], data[1], data[2])
    return str(result)

h, c = 6.63e-34, 3e8

if __name__ == '__main__':
    app.run()


