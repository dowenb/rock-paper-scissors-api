#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS
from random import choice


app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def index():
    return jsonify(Rock="{}shoot/rock".format(request.base_url), Paper="{}shoot/paper".format(request.base_url), Scissors="{}shoot/scissors".format(request.base_url))

@app.route('/shoot/', methods=["GET"])
def instructions():
    return jsonify(Rock="{}rock".format(request.base_url), Paper="{}paper".format(request.base_url), Scissors="{}scissors".format(request.base_url))

@app.route('/shoot/<shot>', methods=["GET"])
def shoot(shot):
    human = shot
    cpu = ComputersShot()
    result = Winner(cpu, human)
    if ValidShot(human):
        return jsonify(Computer=cpu,Human=human,Result=result)
    else:
        return jsonify(Error="Invalid Shot", success=False, Rock="{}rock".format(request.base_url), Paper="{}paper".format(request.base_url), Scissors="{}scissors".format(request.base_url)) #TODO make this return 400 error

def Winner(cpu, human):
    if cpu == human:
        return "Draw"
    elif cpu == 'rock' and human == 'paper':
        return "Human Wins"
    elif cpu == 'paper' and human == 'rock':
        return "CPU Wins"
    elif cpu == 'rock' and human == 'scissors':
        return "CPU Wins"
    elif cpu == 'scissors' and human == 'rock':
        return "Human Wins"
    elif cpu == 'scissors' and human == 'paper':
        return "CPU Wins"
    elif cpu == 'paper' and human == 'scissors':
        return "Human Wins"
    else:
        return "Invalid move" # TODO do checks above, and throw porper exception / return code here

def ComputersShot():
    return choice(['rock','paper','scissors'])

def ValidShot(shot):
    return str.lower(shot) in ['rock', 'paper', 'scissors']

if __name__ == '__main__':
    app.run(debug=True)