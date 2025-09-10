from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route("/about")
def about():
    return '<h1>Om-sida</h1><p>Detta är en enkel Flask-app deployad på Render.</p>'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)