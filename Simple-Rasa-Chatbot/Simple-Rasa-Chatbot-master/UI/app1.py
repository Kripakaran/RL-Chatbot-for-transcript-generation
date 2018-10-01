from flask import Flask
from flask import render_template,jsonify,request
import json,ast
import requests
from models import *
from response import *
import random

@app.route('/')
def hello_world():
    """
    Sample hello world
    """
    return render_template('home.html')

get_random_response = lambda intent:random.choice(response[intent])



@app.route('/chat',methods=["POST"])
def chat():
    """
    chat end point that performs NLU using rasa.ai
    and constructs response from response.py
    """
    try:
        print (request.form["text"])
        response = requests.get("http://localhost:5000/parse",params={"q":request.form["text"]})
        response = response.json()
        jdata = ast.literal_eval(json.dumps(response))
        intent = jdata["intent"]
        intentname=intent["name"]
        if intentname == "Greet":
            response_text="Welcome"
            print ("GREET")
        else:
            response_text = get_random_response(intentname)
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print (e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8000)
