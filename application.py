# Import creates a flask web server and render template () method looks for html files
from flask import Flask, render_template
# We are creating an instance of flask class and call it app.
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
    # return "Hello, World!"
@app.route("/about)
def about():
    return render_template("about.html")
@app.route("/Moses")
def salvador():
    return "Hello, Moses"
# _name_ means this current file. The conditional statement prevents other scripts from running.
# debug = true allows python errors to appear on the web page and help to trace the errors.
if __name__ == "__main__":
    app.run(debug=True)
