from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("Landing_Page.html")


@app.route("/Syafiq")
def Syafiq_Page():
    return render_template("Syafiq-index.html")


@app.route("/Phong")
def Phong_Page():
    return render_template("Phiraphong-index.html")


@app.route("/Ahmad")
def Ahmad_Page():
    return render_template("Ahmad-index.html")


if __name__ == '__main__':
    app.run()
