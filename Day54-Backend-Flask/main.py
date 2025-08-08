from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route("/")
def say_hello():
    return "Hello, Backend World!"

@app.route("/bye")
def say_bye():
    return "Bye, FrontEnd Development!"
@app.route("/<name>")
def say_greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)