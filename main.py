from flask import Flask, request
import ExtractData
import os
import jinja2
from flask_bower import Bower
from Award import Award

# Makes a new file system path by joining the location of the current file to
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

# @ signifies a decorator - a way to wrap a function and modifying it's behaviour
@app.route('/', methods=['GET', 'POST'])
def index():
    template = jinja_env.get_template('index.html')

    if request.method == 'POST':
        currFaculty = request.form['faculty']
        currType = request.form['type']
        awards = ExtractData.passResult(currFaculty, currType)
        template = jinja_env.get_template('index.html')

        return template.render(faculty=currFaculty, type=currType, awards=awards)

    return template.render()

# Kicks the entire app off in our web server
# only if this file had run
if __name__ == "__main__":
    Bower(app.run(debug=True))
