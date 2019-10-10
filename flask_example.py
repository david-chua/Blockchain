from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"

@app.route("/hello", methods=["GET"])
def hola():
    return "Que tal amigo!"

if __name__ == "__main__":
    app.run()
