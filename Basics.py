from flask import Flask, render_template, request
from FruitVision import run

app = Flask(__name__)


@app.route('/')
def index():

    return render_template("profile.html")

@app.route('/test', methods = ['POST'])
def postMethod():

    shelfLife = run(request.form)

    return render_template("profile.html", shelfLife=shelfLife)


if __name__ == "__main__":
    app.run()