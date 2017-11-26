from flask import Flask, request
import ExtractData, os, jinja2
from flask_bower import Bower

# from Award import Award

# Makes a new file system path by joining the location of the current file to
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

# Flash uses cookies, we need a secret key
app.secret_key = 'Manitoba'


# @ signifies a decorator - a way to wrap a function and modifying it's behaviour
@app.route('/', methods=['GET', 'POST'])
def index():
    template = jinja_env.get_template('index.html')
    error = None
    errorMsg = ""
    allFaculty = ""
    allType = ""
    resultMsg = "You have selected: "
    totalAwards = 0
    containsViewAllFac = None
    containsViewAllType = None

    if request.method == 'POST':

        # Both get lists returns an array
        currFaculty = request.form.getlist('faculty[]')
        currType = request.form.getlist('type[]')
        currKeyword = request.form['keyword']
        currAmount = request.form['amount']

        # Checks if the array is not empty
        if currFaculty:
            # Iterate through the list
            for x in currFaculty:
                allFaculty += x + ", "

                if x == 'View all faculties':
                    containsViewAllFac = 1

            allFaculty = allFaculty[:-2]
        else:
            errorMsg += "Please choose faculty, "

        if containsViewAllFac:
            currFaculty = ["View all faculties"]

        if currType:
            for y in currType:
                allType += y + ", "

                if x == 'View all faculties':
                    containsViewAllType = 1

            allType = allType[:-2]
        else:
            errorMsg += "Please choose award type, "

        if containsViewAllType:
            currType = ["View all types"]

        resultMsg += allFaculty + ", " + allType

        if currKeyword != "":
            resultMsg += ", " + currKeyword

        if errorMsg != "":
            error = ""

            # Slice the ", " at the end
            error += errorMsg[:-2]

        if error is None:
            awards = ExtractData.passResult(currFaculty, currType, currKeyword, currAmount)
            totalAwards = ExtractData.getTotal()
            return template.render(awards=awards, searchMsg=resultMsg, awardCount=totalAwards)
        else:
            return template.render(error=error)

    return template.render(searchMsg=None)


# Kicks the entire app off in our web server
# only if this file had run
if __name__ == "__main__":
    Bower(app.run)
