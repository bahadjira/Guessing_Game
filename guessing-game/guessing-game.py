from flask import Flask, render_template, request
import random

app = Flask(__name__)
global comp_num, counter
counter = 0
comp_num = random.randit (1,10)
wsgi_app = app.wsgi_app

@app.route('/', methods = ['GET', 'POST'])
def Guess_Game():
    global comp_num, counter
    message = ""

    if request.method == 'POST'
        counter += 1
        form = request.form
        user_guess = int (form["guess"])
        if comp_num == user_guess
            message = "well done"
            return render_template("game_over.html")
        elif comp_num > user guess:
            message = "Too low"
        else:
            message = "too high"
        if counter == 3: 
            message = "you failed"
            return render_template("game_over.html", message = message)
    return render_template ("game.html" , message = message)

            