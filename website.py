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

@app.route("/wmt")
def wmt():
    return render_template('wmt.html')

@app.route("/lmt")
def lmt():
    return render_template('lmt.html')
    
if __name__ == "__main__":
    while True:
        try:
            app.run(debug=True,host='0.0.0.0')
        except Exception:
            pass
    