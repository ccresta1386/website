from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/image")
def image():
    return render_template('image.html')

@app.route("/home")
def home():
    return render_template('home.html')

    
if __name__ == "__main__":
    app.run(debug=True)
