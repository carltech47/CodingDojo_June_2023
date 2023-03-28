
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<rows>/<columns>')
def changeSquares(rows, columns):
    return render_template("change_squares.html", rows=int(rows), columns=int(columns))


if __name__=="__main__":
    app.run(debug=True)



# Your program should have the following output:
# http://localhost:5000 - should display 8 by 8 checkerboard
# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  
# For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.
