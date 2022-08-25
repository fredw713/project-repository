from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>You're gonna be a good Devops</h1>"

@app.route("/second")
def second():
    return "I'm going to be a AWS Cloud Architect"

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page..Fred</h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'


if __name__ == "__main__":
    app.run(debug=True)