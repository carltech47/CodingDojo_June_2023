from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)     # Create a new install of the Flask class called "app"


@app.route("/play")
def scene_one():
    return render_template("index.html",num=3,color="blue")

@app.route("/play/<int:num>")
def scene_two(num):
    return render_template("index.html",num=num,color="blue")

@app.route("/play/<int:num>/<string:color>")
def scene_three(num, color):
    return render_template("index.html",num=num,color=color)



if __name__=="__main__":
    app.run(debug=True)