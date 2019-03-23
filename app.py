#!flask/bin/python
from flask import Flask
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Rocker Paper Scissors API! 1, 2, 3 /shoot"

@app.route('/shoot')
def shoot(UsersShot  = 'paper'): # TODO allow human to "post" their shot
    cpu = ComputersShot()
    human = UsersShot
    if ValidShot(UsersShot):
        return "CPU: {} Human: {} the result is {}".format(cpu,human,Winner(cpu, human))
    else:
        return "Valid shots include: 'rock', 'paper', 'scissors'" # TODO do not return a 200 OK code here

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