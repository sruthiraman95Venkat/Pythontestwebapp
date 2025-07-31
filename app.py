from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, this is a staging test website!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
