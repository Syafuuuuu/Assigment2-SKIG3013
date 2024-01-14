from flask import Flask, request, redirect, url_for
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("Landing_Page.html")

if __name__ == '__main__':
    app.run()