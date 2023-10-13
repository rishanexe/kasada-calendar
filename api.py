from flask import Flask, jsonify, request
import json
import bcrypt

app = Flask(__name__)

@app.route("/events", methods=["POST"])
def hello_world():
    
    with open('data/auth.json') as file:
        auth = json.load(file)
        if bcrypt.checkpw(request.json["key"].encode('utf8'), auth["key"].encode('utf8')):
            with open('data/calendar.json') as file:
                events = json.load(file)

            return jsonify(events)
        
        else:
            return "<p>Error: Key not valid</p>"
