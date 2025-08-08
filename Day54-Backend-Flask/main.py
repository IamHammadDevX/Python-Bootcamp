from flask import Flask # type: ignore

app = Flask(__name__)

print(__name__)


@app.route("/")
def say_hello():
    return '<h1 style="text-align: center">Hello, Backend World!</h1>'\
            '<p>Hello buddy, its backend</p>' \
            '<img src="Day54-Backend-Flask\pic.jpg" alt="image goes here" >'

@app.route("/bye")
def say_bye():
    return "Bye, FrontEnd Development!"
@app.route("/<name>")
def say_greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)