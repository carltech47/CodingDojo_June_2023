from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)     # Create a new install of the Flask class called "app"

@app.route("/")
def main_page():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)