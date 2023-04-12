from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="CodingDojo is the best"

@app.route('/')
def my_counter():
    if "my_count" not in session:
        session["my_count"] = 0
    else:
        session["my_count"] += 1
    return render_template("index.html")

@app.route('/reset')
def increment():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)