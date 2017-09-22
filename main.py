from flask import Flask, request, render_template
import ExtractData
app = Flask(__name__)

# @ signifies a decorator - a way to wrap a function and modifying it's behaviour
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/searchResult',  methods=['GET','POST'])
def searchResult():
    currFaculty = request.form['faculty']
    currType = request.form['type']


    stuff = ExtractData.passResult(currFaculty, currType)

    #stuff = ExtractData.passResult()

    return render_template("searchResult.html", passResult=stuff, faculty=currFaculty, type=currType)

# Kicks the entire app off in our web server
# only if this file had run
if __name__ == "__main__":
    app.run(debug=True)