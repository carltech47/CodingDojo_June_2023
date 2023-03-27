from flask import Flask, render_template
app = Flask(__name__)

#@app.route("/")
#def main_page():
#    return render_template("index.html")

@app.route('/')
def main_page():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<my_name>')
def my_hi(my_name):
    return f"Hi {my_name}!"

@app.route('/repeat/<int:num>/<string:my_word>')
def my_repeat(num,my_word):
    return render_template("index.html",num=num,my_word=my_word)

if __name__=="__main__":
    app.run(debug=True)



