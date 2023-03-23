from flask import Flask
app = Flask(__name__)

@app.route("/hi")
def hello_route():
    return "Hello from Flask!"

if __name__=="__main__":
    app.run(debug=True)