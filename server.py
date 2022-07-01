from flask import Flask, render_template, request, redirect,session
import random
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    info = {
        "message": None,
        "css_color": None
    }
    if "number" not in session:
        session["number"]= random.randint(1,100)
    if "tries" not in session:
        session["tries"] = 0

    if "guess" not in session:
        info["message"] = "Ready!"
        info["css_color"] = "dark"
    elif int(session["tries"]) > 4:
        info['message'] = "You Lose!"
        info['css_color'] = "red"
    
    elif int(session["guess"]) > int(session["number"]):
        info["message"] = 'Too high!'
        info['css_color'] = "red"
    elif int(session["guess"]) < int(session["number"]):
        info['message'] = "Too Low!"
        info['css_color'] = "red"
    elif int(session["guess"]) == int(session["number"]):
        info['message'] = f"{session['number']} was the number!"
        info['css_color'] = "green" 
    return render_template("index.html", info = info)


@app.route('/guessed_num', methods=['POST'])
def create_user():
    session["guess"] = request.form['guessed_number']    
    session['tries'] += 1
    return redirect('/')

@app.route('/reset', methods=['GET','POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)