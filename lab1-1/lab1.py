from flask import Flask, jsonify, request
import json

app = Flask(__name__)

global data

with open("data.json") as f:
    data = json.load(f)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/students")
def get_students():
    results = []
    pref = request.args.get('pref')
    if pref:
        for student in data:
            if student['pref'] == pref:
                results.append(student)
        return jsonify(results)
    return jsonify(data)

@app.route("/students/<uid>")
def get_student(uid):
    for student in data:
        if student['id'] == uid:
            return jsonify(student)

@app.route("/stats")
def get_stats():
    stats = {
        "Chicken": 0,
        "Computer Science (Major)": 0,
        "Computer Science (Special)": 0,
        "Fish": 0,
        "Information Technology (Major)": 0,
        "Information Technology (Special)": 0,
        "Vegetable": 0
    }

    if data:
        for student in data:
            if student["pref"] in stats.keys():
                stats[student["pref"]] = stats[student["pref"]] + 1
            if student["programme"] in stats.keys():
                stats[student["programme"]] = stats[student["programme"]] + 1
        return jsonify(stats)

@app.route('/add/<a>/<b>')
def add(a, b):
    return str(int(a) + int(b))

@app.route('/subtract/<a>/<b>')
def sub(a, b):
    return str(int(a) - int(b))

@app.route('/multiply/<a>/<b>')
def mul(a, b):
    return str(int(a) * int(b))

@app.route('/divide/<a>/<b>')
def div(a, b):
    return str(int(a) / int(b))

app.run(host="0.0.0.0", port=8080)
