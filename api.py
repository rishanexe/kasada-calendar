from flask import Flask, jsonify, request
import json
import bcrypt

app = Flask(__name__)

@app.route("/get-events", methods=["POST"])
def get_events():
    # "/home/kasada/mysite/auth.json"
    with open('data/auth.json') as file:
        auth = json.load(file)
        if bcrypt.checkpw(request.json["key"].encode('utf8'), auth["key"].encode('utf8')):
            # "/home/kasada/mysite/calendar.json"
            with open('data/calendar.json') as file:
                events = json.load(file)

            return jsonify(events)
        
        else:
            return jsonify({"Error": "Key not valid"})
        

@app.route("/update-events", methods=["POST"])
def update_events():
    # "/home/kasada/mysite/auth.json"
    with open('data/auth.json') as file:
        auth = json.load(file)
        if bcrypt.checkpw(request.json["key"].encode('utf8'), auth["key"].encode('utf8')):
            # "/home/kasada/mysite/calendar.json"
            with open('data/calendar.json', 'w') as file:
                json.dump(request.json["data"], file)

            return "<p>Success: Calendar events updated</p>"
        
        else:
            return "<p>Error: Key not valid</p>"
