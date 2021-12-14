import json
from urllib.request import urlopen
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/plus/<int:a>/<int:b>")
def add_ws(a, b): # web service
    return jsonify({"result": a+b})

@app.route("/plus/<int:a>/<int:b>")
def add(a, b): # web application
    return f"{a} + {b} = {call_ws('plus',a,b)}"

@app.route("/api/minus/<int:a>/<int:b>")
def minus_ws(a, b): # web service
    return jsonify({"result": a-b})

@app.route("/minus/<int:a>/<int:b>")
def minus(a, b): # web application        
    return f"{a} - {b} = {call_ws('minus',a,b)}"

def call_ws(op, a, b):
    # use appropriate api url based on the operation passed as argument
    if op=='plus':
        with urlopen(f"http://localhost:5000/api/plus/{a}/{b}") as resp:
            json_data = resp.read().decode("utf-8")
            resp = json.loads(json_data)
            result = resp["result"] #change to return a value
    elif op=='minus':
        with urlopen(f"http://localhost:5000/api/minus/{a}/{b}") as resp:
            json_data = resp.read().decode("utf-8")
            resp = json.loads(json_data)
            result = resp["result"] #change to return a value
    # Return the result
    return result


if __name__ == "__main__":
    app.run()